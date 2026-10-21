from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet_transaction import WalletTransaction, WalletTransactionDict


class WalletGrantResultResponse(SdkBaseModel):
    """Returned by an adjustment: the ledger row written, plus the wallet's new balance."""

    wallet_transactions: list[WalletTransaction]
    balance: str
    """The wallet's new balance, as a decimal string."""


class WalletGrantResultResponseDict(TypedDict):
    wallet_transactions: list[WalletTransactionDict]
    balance: str
