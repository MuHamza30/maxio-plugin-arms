from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.kind1 import Kind1OrStr
from .unions.amount6 import Amount6, Amount6Dict


class WalletTransaction1(SdkBaseModel):
    kind: Kind1OrStr
    """Determines the direction of the movement. The amount itself is always sent positive."""

    amount: Amount6
    """Always positive; ``kind`` determines the sign written to the ledger. Encoded as a decimal string with at most 8
    fractional digits. Send fractional values as strings: a JSON number with a decimal point is rejected with ``422``,
    because a double-precision float may already have lost precision before the request arrives."""

    memo: OptionalNullable[str] = UNSET
    expires_at: OptionalNullable[str] = UNSET
    """An expiration for the grant this creates. Only accepted with ``kind: grant``; sending it with ``kind: debit`` is
    rejected. Omit it for an evergreen grant. Accepts either a bare calendar date (``YYYY-MM-DD``), resolved to the end
    of that day in the site's time zone, or a full timestamp. A calendar day that doesn't exist, such as ``2027-02-30``,
    is rejected with ``422`` rather than rolled into the next month."""


class WalletTransaction1Dict(TypedDict):
    kind: Kind1OrStr
    amount: Amount6Dict
    memo: NotRequired[str | None]
    expires_at: NotRequired[str | None]
