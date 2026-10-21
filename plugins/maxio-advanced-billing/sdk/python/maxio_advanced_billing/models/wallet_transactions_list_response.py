from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list_public_keys_meta import ListPublicKeysMeta, ListPublicKeysMetaDict
from .wallet_transaction import WalletTransaction, WalletTransactionDict


class WalletTransactionsListResponse(SdkBaseModel):
    wallet_transactions: list[WalletTransaction]
    meta: ListPublicKeysMeta


class WalletTransactionsListResponseDict(TypedDict):
    wallet_transactions: list[WalletTransactionDict]
    meta: ListPublicKeysMetaDict
