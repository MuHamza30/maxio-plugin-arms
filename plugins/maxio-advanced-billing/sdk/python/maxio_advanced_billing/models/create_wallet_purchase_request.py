from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .purchase import Purchase, PurchaseDict


class CreateWalletPurchaseRequest(SdkBaseModel):
    """Purchases prepaid units for the wallet at a price point, charging the subscription's payment method."""

    purchase: Purchase


class CreateWalletPurchaseRequestDict(TypedDict):
    purchase: PurchaseDict
