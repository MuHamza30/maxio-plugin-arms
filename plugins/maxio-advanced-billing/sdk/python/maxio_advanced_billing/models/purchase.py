from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .unions.quantity4 import Quantity4, Quantity4Dict


class Purchase(SdkBaseModel):
    quantity: Quantity4
    """The number of wallet units to purchase, as a decimal string with at most 8 fractional digits. Send fractional
    values as strings: a JSON number with a decimal point is rejected with ``422``, because a double-precision float may
    already have lost precision before the request arrives."""

    price_point_id: Optional[int] = UNSET
    """The price point to purchase at. Must belong to the wallet's billing product. Defaults to the ``price_point_id``
    set on the wallet."""

    memo: OptionalNullable[str] = UNSET
    """(Optional) A note recorded on the resulting grant's ledger row."""


class PurchaseDict(TypedDict):
    quantity: Quantity4Dict
    price_point_id: NotRequired[int]
    memo: NotRequired[str | None]
