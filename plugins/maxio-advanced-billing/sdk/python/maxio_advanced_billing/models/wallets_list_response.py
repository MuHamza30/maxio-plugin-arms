from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list_public_keys_meta import ListPublicKeysMeta, ListPublicKeysMetaDict
from .wallet import Wallet, WalletDict


class WalletsListResponse(SdkBaseModel):
    wallets: list[Wallet]
    meta: ListPublicKeysMeta


class WalletsListResponseDict(TypedDict):
    wallets: list[WalletDict]
    meta: ListPublicKeysMetaDict
