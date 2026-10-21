from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet_product_active_wallet import WalletProductActiveWallet, WalletProductActiveWalletDict


class ActiveWallets(SdkBaseModel):
    total: int
    """Total count of active wallets drawing on this product."""

    sample: list[WalletProductActiveWallet]
    """Up to 50 of the most recently created active wallets, newest first."""


class ActiveWalletsDict(TypedDict):
    total: int
    sample: list[WalletProductActiveWalletDict]
