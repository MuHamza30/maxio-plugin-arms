from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet_purchase import WalletPurchase, WalletPurchaseDict


class WalletPurchaseResultResponse(SdkBaseModel):
    wallet_purchases: list[WalletPurchase]
    balance: str
    """The wallet's new balance, as a decimal string."""


class WalletPurchaseResultResponseDict(TypedDict):
    wallet_purchases: list[WalletPurchaseDict]
    balance: str
