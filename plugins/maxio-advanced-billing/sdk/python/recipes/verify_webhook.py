"""Webhook signature check for Maxio Advanced Billing.

Synchronous and pure: no I/O, no lock. Call it from sync or async code alike.

What it does
- `verify_webhook(raw_body, signature, shared_key)` is True only when `signature` is the hex HMAC-SHA256
  of `raw_body` under the site's shared key. Upper and lower case hex both pass. The comparison takes the
  same time wherever the two values differ. A missing, empty, non-hex, wrong-length or non-ASCII
  signature gives False, never an exception.
- `signature_from_headers(headers)` finds the signature whatever the case of the header name, in the
  forms Python servers hand headers over: a mapping of names to values, a WSGI `environ`
  (`HTTP_X_CHARGIFY_WEBHOOK_SIGNATURE_HMAC_SHA_256`), or the ASGI list of `(name, value)` pairs. Names and
  values may be `str` or `bytes`.

The body must be the bytes as received, before any parsing. Maxio signs the form-encoded bytes it sent
(`payload[subscription][id]=...`). A body that was parsed and encoded again never matches.

What it does not do
- It does not read the request. You pass the raw bytes and the headers.
- It does not answer the webhook, and it does not skip a webhook `id` you already processed. Answer 200
  within about 15 seconds for every event, also the ones you do not handle, and do the work afterwards.
- It does not load the shared key. Keep one key per site in secret storage. An empty key raises
  ValueError instead of returning False, because an unset secret must stop the deployment.
- It does not re-read the resource. A webhook is a hint: read the subscription again before you act
  on the state an event reports.
- It does not read a signature from the query string. When the endpoint URL was registered with the
  `{signature_hmac_sha_256}` replacement variable, pass that query value as `signature` yourself.

Rules: knowledge/rules.md R19. It leaves R20 to you.

Copy into your project and adapt. Not part of the SDK's API. Needs only the standard library.
"""

from __future__ import annotations

import hashlib
import hmac
import string
from collections.abc import Iterable, Mapping, Sequence
from typing import Final, TypeAlias, cast

SIGNATURE_HEADER: Final = "X-Chargify-Webhook-Signature-Hmac-Sha-256"

_HEADER_KEY: Final = SIGNATURE_HEADER.lower()
_HEX_LENGTH: Final = hashlib.sha256().digest_size * 2
_HEX_DIGITS: Final = frozenset(string.hexdigits)

Headers: TypeAlias = Mapping[str, object] | Mapping[bytes, object] | Iterable[Sequence[object]]


def verify_webhook(raw_body: bytes, signature: str | bytes | None, shared_key: str) -> bool:
    """True only when `signature` is Maxio's signature of `raw_body` under `shared_key`.

    Call it before you parse the body.

    Args:
        raw_body: The request body as received.
        signature: The value of SIGNATURE_HEADER, as `str` or `bytes`, or None when the header is absent.
            `signature_from_headers` gets it for you.
        shared_key: The site's shared key.

    Raises:
        ValueError: `shared_key` is empty.
        TypeError: `raw_body` is not bytes. A decoded body cannot be checked.
    """
    if not shared_key:
        raise ValueError("the Maxio webhook shared key is empty")
    if not _is_bytes(raw_body):
        raise TypeError("raw_body must be the request body as bytes, exactly as received")
    claimed = _digest_from_hex(signature)
    if claimed is None:
        return False
    expected = hmac.digest(shared_key.encode("utf-8"), raw_body, hashlib.sha256)
    # `==` stops at the first differing byte, which lets a sender learn a valid signature one byte at a
    # time. compare_digest does not.
    return hmac.compare_digest(expected, claimed)


def signature_from_headers(headers: Headers) -> str | bytes | None:
    """The signature header's value, or None when the request has none.

    Takes a mapping (a framework's `request.headers`, a plain dict, a WSGI `environ`) or an iterable of
    `(name, value)` pairs (ASGI's `scope["headers"]`, or `.items()` of anything else). The name is matched
    without regard to case. With a repeated header the first value is returned.
    """
    for pair in _pairs(headers):
        if len(pair) != 2:
            continue
        name, value = pair[0], pair[1]
        if _is_signature_header(name) and isinstance(value, (str, bytes)):
            return value
    return None


def _pairs(headers: Headers) -> Iterable[Sequence[object]]:
    if isinstance(headers, Mapping):
        return cast("Mapping[object, object]", headers).items()
    return headers


def _is_bytes(value: object) -> bool:
    # A function of its own, so a type checker does not call the check redundant. It is for callers no
    # checker saw, who pass the body after decoding it.
    return isinstance(value, (bytes, bytearray, memoryview))


def _is_signature_header(name: object) -> bool:
    if isinstance(name, bytes):
        name = name.decode("latin-1")
    if not isinstance(name, str):
        return False
    # WSGI spells a header HTTP_X_CHARGIFY_...; every other form differs from ours by case alone.
    key = name.lower().replace("_", "-")
    return key == _HEADER_KEY or key == "http-" + _HEADER_KEY


def _digest_from_hex(signature: str | bytes | None) -> bytes | None:
    """The 32 digest bytes a well-formed signature names, or None for anything else."""
    if isinstance(signature, bytes):
        try:
            signature = signature.decode("ascii")
        except UnicodeDecodeError:
            return None
    if not isinstance(signature, str):
        return None
    text = signature.strip()
    # Checked by hand: bytes.fromhex skips spaces and compare_digest raises on a non-ASCII str, and a
    # hostile header must be a rejection, not a server error.
    if len(text) != _HEX_LENGTH or not _HEX_DIGITS.issuperset(text):
        return None
    return bytes.fromhex(text)
