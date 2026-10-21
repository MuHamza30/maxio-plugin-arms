"""Request limit for Maxio Advanced Billing: at most four requests in flight per site.

Synchronous: a caller waits for a slot by blocking its thread. Never enter it on an asyncio event loop
(it raises there). From async code, run the whole call in a worker thread with `asyncio.to_thread` and
take the slot inside that thread (recipes/README.md, "From async code").

What it does
- `with maxio_slot(site):` holds one of the site's four slots while the block runs. A fifth caller
  waits. Waiters are served first come, first served: a released slot goes to the caller that has
  waited longest, and a caller that arrives later cannot take it first.
- `wait_seconds` bounds the wait. When it runs out the caller gets SlotTimeout and nothing was sent.
  Python threads cannot be cancelled, so this is the only way a waiter gives up.
- Nested use in one thread is safe: a block entered while the thread already holds a slot for that
  site uses the same slot. So you may wrap a helper that makes several calls one after another
  (recipes/list_all.py, recipes/safe_signup.py), and that helper may wrap its own calls again.

What the limit covers, exactly
- Slots are counted in this process, per site name. Other processes, other hosts and other programs
  that call the same Maxio site are not counted. Maxio's limit is per subdomain across all of them.
- A slot is released when the block ends, which is when the SDK call returns or raises. After a client
  timeout that can be before Maxio has finished: Maxio works on a request for up to 120 seconds, so for
  that time it may count one more request than this file does.
- The SDK's own automatic retries run inside the block and keep the slot while they wait. They add
  no request in flight.
- NOT SAFE: a thread that holds a slot and waits for another thread that needs a slot of the same
  site. Four such threads hold all four slots and wait for ever. Take the slot in the thread that
  makes the call, and give `wait_seconds` wherever this could happen, so the mistake shows as
  SlotTimeout and not as a hang.

The two client options this SDK needs for Maxio (the limit above does not replace them)
`maxio_retry_options()` returns both at once: the SDK's default retry policy, or the one you pass, with
429 removed from the statuses to retry and PUT removed from the methods to retry. Build the client with
`retry_options=maxio_retry_options()`. Written out:
- No automatic retry of a 429. By default the SDK sends a GET, HEAD, PUT or OPTIONS again after about
  1, 2 and 4 seconds when the answer is 429. Maxio asks for a pause of minutes (knowledge/rules.md R10).
  Build the client without 429 in the statuses to retry:
      retry_options={"status_codes_to_retry": frozenset({408, 500, 502, 503, 504})}
- No automatic retry of a PUT. By default the SDK treats PUT as safe to send again, also after a
  timeout. `retry_subscription`, `reactivate_subscription` and `activate_subscription` are PUTs that can
  take a payment, `update_subscription` can when it carries payment details, and `verify_bank_account`
  is capped at ten attempts (knowledge/rules.md R11). Build the client without PUT in the methods to
  retry:
      retry_options={"http_methods_to_retry": frozenset({"GET", "HEAD", "OPTIONS"})}
  or turn retry off for one call, whatever the client's policy:
      request_options={"max_retries": 0}
  Both client options go in one `retry_options` mapping. recipes/README.md shows the whole client.
  Everything else in the SDK's policy stays: a GET that answers 408 or 5xx, or gets no answer, is
  still sent again up to three times.

What it does not do
- It does not pause after a 429. Stop sending new work to that site for a few minutes, then go slower.
- It does not share the limit between processes or hosts. Give each process a share of the four
  (lower MAX_IN_FLIGHT), or put one shared limiter in front of them.
- It does not retry anything and does not time a call out.

Rules: knowledge/rules.md R10, R11

Copy into your project and adapt. Not part of the SDK's API. Needs the SDK and the standard library.
"""

from __future__ import annotations

import asyncio
import threading
from collections import deque
from collections.abc import Generator
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Final

from maxio_advanced_billing.core import RetryOptions

MAX_IN_FLIGHT: Final = 4  # Maxio's limit on concurrent requests per subdomain


def maxio_retry_options(base: RetryOptions | None = None) -> RetryOptions:
    """The client's retry policy for Maxio: `base` without 429 among the statuses to retry and without PUT
    among the methods to retry. None means the SDK's default policy. Every other term stays as it was.

        client = MaxioAdvancedBillingClient(retry_options=maxio_retry_options(), ...)
    """
    policy = base if base is not None else RetryOptions()
    return policy.model_copy(
        update={
            "status_codes_to_retry": policy.status_codes_to_retry - {429},
            "http_methods_to_retry": policy.http_methods_to_retry - {"PUT"},
        }
    )


class SlotTimeout(TimeoutError):
    """No slot came free within `wait_seconds`. Nothing was sent."""


@dataclass(frozen=True)
class SlotUsage:
    """What one site's gate looks like right now. For logs and metrics."""

    in_flight: int
    waiting: int


class _Gate:
    """A number of slots and a queue. A released slot is handed to the head of the queue and is never
    free while someone waits, so no later arrival can take it first."""

    def __init__(self, slots: int) -> None:
        self._slots = slots
        self._free = slots
        self._waiters: deque[threading.Event] = deque()
        self._lock = threading.Lock()

    def acquire(self, wait_seconds: float | None) -> bool:
        with self._lock:
            if self._free > 0:  # a slot is free only when no one waits
                self._free -= 1
                return True
            ticket = threading.Event()
            self._waiters.append(ticket)
        try:
            if ticket.wait(wait_seconds):
                return True
        except BaseException:  # Ctrl-C while waiting: leave the queue, and pass on a slot that just arrived
            self._give_up(ticket, keep_slot=False)
            raise
        return self._give_up(ticket, keep_slot=True)

    def _give_up(self, ticket: threading.Event, *, keep_slot: bool) -> bool:
        """Leave the queue. True when a slot was handed over in the meantime and is kept."""
        with self._lock:
            if not ticket.is_set():
                self._waiters.remove(ticket)
                return False
            if not keep_slot:
                self._release_locked()
            return keep_slot

    def release(self) -> None:
        with self._lock:
            self._release_locked()

    def _release_locked(self) -> None:
        if self._waiters:
            self._waiters.popleft().set()  # the slot changes hands; it is not free in between
        else:
            self._free += 1

    def usage(self) -> SlotUsage:
        with self._lock:
            return SlotUsage(in_flight=self._slots - self._free, waiting=len(self._waiters))


class _HeldByThread(threading.local):
    """How many nested blocks this thread has open, per site."""

    def __init__(self) -> None:
        self.depth: dict[str, int] = {}


_gates: dict[str, _Gate] = {}
_gates_lock = threading.Lock()
_held = _HeldByThread()


def _site_key(site: str) -> str:
    key = site.strip().lower()  # subdomains are case-insensitive; two spellings must share one gate
    if not key:
        raise ValueError("site is empty: pass the Maxio subdomain")
    return key


def _gate_for(key: str) -> _Gate:
    with _gates_lock:
        gate = _gates.get(key)
        if gate is None:
            gate = _gates[key] = _Gate(MAX_IN_FLIGHT)
        return gate


def _refuse_event_loop() -> None:
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return  # no loop runs in this thread: the normal case
    raise RuntimeError(
        "maxio_slot is synchronous and was entered on an asyncio event loop, where it would block every "
        "task and count them all as one thread. Run the call with asyncio.to_thread and take the slot there."
    )


@contextmanager
def maxio_slot(site: str, *, wait_seconds: float | None = None) -> Generator[None, None, None]:
    """Hold one of the site's four slots for as long as the `with` block runs.

        with maxio_slot("acme"):
            found = client.subscriptions.read_subscription(subscription_id)

    Args:
        site: The Maxio subdomain, the value the client's server configuration has as `site`. Case and
            surrounding spaces do not matter. Every caller of one site must pass the same name.
        wait_seconds: The longest to wait for a free slot. None waits without limit. 0 does not wait.

    Raises:
        SlotTimeout: No slot came free within `wait_seconds`. Nothing was sent.
        RuntimeError: Entered on an asyncio event loop.
        ValueError: `site` is empty.
    """
    key = _site_key(site)
    _refuse_event_loop()
    depth = _held.depth
    if depth.get(key, 0) > 0:  # nested in this thread: its calls run one after another on the slot it holds
        depth[key] += 1
        try:
            yield
        finally:
            depth[key] -= 1
        return
    gate = _gate_for(key)
    if not gate.acquire(wait_seconds):
        raise SlotTimeout(f"no free Maxio request slot for site {key!r} within {wait_seconds} s")
    depth[key] = 1
    try:
        yield
    finally:
        del depth[key]
        gate.release()


def slot_usage(site: str) -> SlotUsage:
    """Requests in flight and callers waiting for `site`, as this process counts them."""
    return _gate_for(_site_key(site)).usage()
