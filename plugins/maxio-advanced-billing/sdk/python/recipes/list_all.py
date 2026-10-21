"""Page a Maxio list operation to the end.

Synchronous: every page is a blocking SDK call. From async code run the whole walk with
`asyncio.to_thread` (recipes/README.md, "From async code").

What it does
- `list_all(fetch_page, max_pages=...)` reads a list that takes `page` and `per_page` and returns an
  array. It starts at page 1 and asks for 200 rows a page, Maxio's cap. The SDK does not page for you:
  a list call returns the one page you asked for, and with `per_page` left out it sends the spec
  default (20 on most lists), so an unpaged call returns a fraction of the data and no error.
- It stops only on an empty page. A short page is not the end: a list whose own cap is below what
  you asked for returns short pages all the way.
- `per_page` is 200 unless you pass less. Pass less only for an operation whose maximum is lower
  (`list_mrr_movements` stops at 50).
- `max_pages` is a ceiling on requests, the final empty page included. Reaching it raises
  PageCeilingReached. Nothing is returned then, so a cut-off list can never pass for the whole one.
- With `key`, a row whose key was already seen is dropped. A list that shifts while you walk it (a row
  is added before your position) then yields no row twice.

What it does not do
- It cannot stop a shifting list from hiding a row: when a row before your position is removed, the
  next row moves back onto a page you have read. Ask for a sort that does not move where the operation
  offers one. `list_all_subscriptions` below sorts by id, ascending.
- It does not check your filters. knowledge/rules.md R9 names the ones that fail open.
- It does not limit requests in flight. The walk is sequential, so one slot around the whole walk is
  enough (recipes/request_limit.py).
- It does not retry a failed page. The SDK error propagates and no rows are returned.

Adapting it
- A list that returns a wrapper object: unwrap it in `fetch_page`.
      invoices = list_all(
          lambda page, per_page: client.invoices.list_invoices(page=page, per_page=per_page).invoices,
          max_pages=500,
          key=lambda invoice: invoice.uid,
      )
- Some list operations take no `page` parameter (`list_customer_subscriptions`,
  `list_subscription_components`, `list_product_families` and others). Call them once. In a loop every
  request would be the same, the same rows would come back, and the walk would end at the ceiling with
  PageCeilingReached. The signature on the SDK map (sdk-map.md, then the operation's page under
  map/operations/) shows whether `page` and `per_page` exist.

A subscription with no product cannot be decoded by this SDK
- On a site with Maxio's new Catalog experience a subscription can have no product. Maxio then
  returns `product`, `product_price_point_id` and `product_price_point_type` as null. This SDK types
  those three fields without null, so it raises pydantic.ValidationError for the whole response. For a
  list page that means the whole page, the good rows included, and this walk raises with it.
- What you can do: build the client over `PlanlessSubscriptionTransport` (below). It removes those
  three nulls before the SDK decodes the answer, so the fields read as UNSET. It is a workaround for an
  SDK limitation, in recipe code, and no part of the SDK. Remove it when the SDK accepts the nulls.

Rules: knowledge/rules.md R8. It leaves R9 to you.

Copy into your project and adapt. Not part of the SDK's API. Needs the SDK and the standard library.
"""

from __future__ import annotations

import json
from collections.abc import Callable, Hashable, Iterator, Mapping, Sequence
from typing import Final, TypeVar, cast

from maxio_advanced_billing import MaxioAdvancedBillingClient, models
from maxio_advanced_billing.core import HttpClient, HttpRequest, HttpResponse, UnsetType
from maxio_advanced_billing.models.enums import SortingDirection, SubscriptionSort

T = TypeVar("T")

PER_PAGE: Final = 200  # Maxio's cap on per_page. A larger value returns 200 rows and no error.


class PageCeilingReached(RuntimeError):
    """The walk used up `max_pages` before Maxio returned an empty page. No rows are returned."""

    def __init__(self, max_pages: int, rows_read: int) -> None:
        super().__init__(f"read {rows_read} rows in {max_pages} pages without reaching an empty page")
        self.max_pages = max_pages
        self.rows_read = rows_read


def list_all(
    fetch_page: Callable[[int, int], Sequence[T]],
    *,
    max_pages: int,
    per_page: int = PER_PAGE,
    key: Callable[[T], Hashable | None] | None = None,
) -> list[T]:
    """Read every page of one list. `fetch_page(page, per_page)` makes the SDK call for one page.

    Args:
        fetch_page: Returns the rows of the page it is handed. Pages start at 1.
        max_pages: The most requests to make, the final empty page included. A list of N full pages
            needs at least N + 1.
        per_page: Rows to ask for per page, 1 to 200.
        key: Returns what identifies a row, such as its id. A row whose key was seen before is dropped.
            A row whose key is None or UNSET has no identity and is always kept.

    Raises:
        PageCeilingReached: Page `max_pages` still had rows.
        ValueError: `max_pages` is below 1, or `per_page` is outside 1 to 200.
    """
    if max_pages < 1:
        raise ValueError("max_pages must be at least 1")
    if not 1 <= per_page <= PER_PAGE:
        raise ValueError(f"per_page must be between 1 and {PER_PAGE}: Maxio clamps a larger value without an error")
    rows: list[T] = []
    seen: set[Hashable] = set()
    for page in range(1, max_pages + 1):
        batch = fetch_page(page, per_page)
        if len(batch) == 0:  # the only end signal
            return rows
        for row in batch:
            identity = key(row) if key is not None else None
            if identity is not None and not isinstance(identity, UnsetType):
                if identity in seen:
                    continue
                seen.add(identity)
            rows.append(row)
    raise PageCeilingReached(max_pages, len(rows))


def list_all_subscriptions(
    client: MaxioAdvancedBillingClient, *, max_pages: int
) -> list[models.SubscriptionResponse]:
    """Every subscription on the site, each as the `{"subscription": ...}` wrapper Maxio sends.

    Sorted by id, ascending, so a subscription created during the walk lands after the pages already
    read (inferred from ids growing). Rows are keyed by subscription id, so none comes back twice.
    Add your filters as keyword arguments to the call below. Raises pydantic.ValidationError when a
    page holds a subscription with no product, unless the client was built over
    `PlanlessSubscriptionTransport`.
    """
    return list_all(
        lambda page, per_page: client.subscriptions.list_subscriptions(
            page=page, per_page=per_page, sort=SubscriptionSort.ID, direction=SortingDirection.ASC
        ),
        max_pages=max_pages,
        key=_subscription_id,
    )


def _subscription_id(row: models.SubscriptionResponse) -> int | UnsetType:
    subscription = row.subscription
    return subscription if isinstance(subscription, UnsetType) else subscription.id


# --- Workaround for an SDK limitation: subscriptions with no product -----------------------------

# Maxio sends these three as null for a subscription with no product. The SDK's Subscription model
# has no null for them and rejects the whole response.
_NULL_FOR_PLANLESS: Final = ("product", "product_price_point_id", "product_price_point_type")


class PlanlessSubscriptionTransport:
    """An HTTP transport for the SDK client that lets subscriptions with no product decode.

        from maxio_advanced_billing.core import Httpx2Client

        client = MaxioAdvancedBillingClient(
            custom_http_client=PlanlessSubscriptionTransport(Httpx2Client(timeout=30.0)),
            ...
        )

    It wraps another transport and changes one thing: in a 2xx JSON answer, inside every object held
    under a `"subscription"` key, it removes `product`, `product_price_point_id` and
    `product_price_point_type` when their value is null. The SDK then decodes the subscription and
    those fields are UNSET. That covers every operation that answers with `{"subscription": {...}}` or
    a list of them: read, find, list, create, update. It does not cover a subscription sent without
    that wrapper (`list_exported_subscriptions`).

    Everything else passes through untouched: other answers byte for byte, error answers, and the
    request. An answer it does change is written again with the `json` module, so its bytes differ
    (1.10 becomes 1.1), but the SDK, which parses with the same module, reads the same values from it.
    The `content-length` header still names the original size; the SDK does not read it.

    The client's own `timeout=` argument is not used when you pass a transport, so give the timeout to
    `Httpx2Client`. Closing the client closes the wrapped transport. Synchronous client only.
    """

    def __init__(self, inner: HttpClient) -> None:
        self._inner = inner

    def send(self, request: HttpRequest) -> HttpResponse:
        return _WithoutNullProducts(self._inner.send(request))

    def close(self) -> None:
        self._inner.close()


class _WithoutNullProducts:
    """The wrapped response, with `read` filtered. The SDK's JSON decoding reads a body through `read`."""

    def __init__(self, inner: HttpResponse) -> None:
        self._inner = inner

    @property
    def url(self) -> str:
        return self._inner.url

    @property
    def status_code(self) -> int:
        return self._inner.status_code

    @property
    def headers(self) -> Mapping[str, str]:
        return self._inner.headers

    def iter_bytes(self, chunk_size: int | None) -> Iterator[bytes]:
        return self._inner.iter_bytes(chunk_size)

    def read(self) -> bytes:
        content = self._inner.read()
        if 200 <= self._inner.status_code < 300:
            return _drop_null_products(content)
        return content

    def close(self) -> None:
        self._inner.close()


def _drop_null_products(content: bytes) -> bytes:
    if b'"product' not in content or b"null" not in content:
        return content  # nothing to remove: the usual case, and the bytes stay as they were
    try:
        document: object = json.loads(content)
    except ValueError:
        return content  # not JSON: the SDK reports it as it would have
    changed = False
    pending: list[object] = [document]
    while pending:
        node = pending.pop()
        if isinstance(node, list):
            pending.extend(cast("list[object]", node))
        elif isinstance(node, dict):
            fields = cast("dict[str, object]", node)
            subscription = fields.get("subscription")
            if isinstance(subscription, dict):
                held = cast("dict[str, object]", subscription)
                for name in _NULL_FOR_PLANLESS:
                    if name in held and held[name] is None:
                        del held[name]
                        changed = True
            pending.extend(fields.values())
    return json.dumps(document).encode("utf-8") if changed else content
