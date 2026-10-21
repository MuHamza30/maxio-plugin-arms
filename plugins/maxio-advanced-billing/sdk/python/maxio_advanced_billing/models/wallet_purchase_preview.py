from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WalletPurchasePreview(SdkBaseModel):
    """A price quote for a purchase, without charging anything."""

    price_point_id: int
    currency: str
    """The three-letter currency code the ``amount`` is denominated in, matching the subscription's currency."""

    quantity: str
    """The number of units the quote is for, as a decimal string."""

    amount: str
    """The price for ``quantity`` units at this price point, as a decimal string."""


class WalletPurchasePreviewDict(TypedDict):
    price_point_id: int
    currency: str
    quantity: str
    amount: str
