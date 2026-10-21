from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WalletProductUsageCount(SdkBaseModel):
    """A rollup of what's using this Wallet Product, for the catalog listing."""

    wallet_configurations: int
    """Number of wallet templates billing through this product, whether or not any wallet has been created from them
    yet."""

    active_wallets: int
    """Number of active (non-archived) wallets currently denominated by this product."""


class WalletProductUsageCountDict(TypedDict):
    wallet_configurations: int
    active_wallets: int
