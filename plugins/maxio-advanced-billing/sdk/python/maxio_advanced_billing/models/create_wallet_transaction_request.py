from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet_transaction1 import WalletTransaction1, WalletTransaction1Dict


class CreateWalletTransactionRequest(SdkBaseModel):
    wallet_transaction: WalletTransaction1


class CreateWalletTransactionRequestDict(TypedDict):
    wallet_transaction: WalletTransaction1Dict
