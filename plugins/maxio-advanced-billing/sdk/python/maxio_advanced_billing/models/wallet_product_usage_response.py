from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .active_wallets import ActiveWallets, ActiveWalletsDict
from .wallet_product_usage_template import WalletProductUsageTemplate, WalletProductUsageTemplateDict


class WalletProductUsageResponse(SdkBaseModel):
    wallet_templates: list[WalletProductUsageTemplate]
    """Wallet templates billing through this product at its default price point."""

    price_point_overrides: list[WalletProductUsageTemplate]
    """Wallet templates billing through this product at a price point other than the default."""

    active_wallets: ActiveWallets


class WalletProductUsageResponseDict(TypedDict):
    wallet_templates: list[WalletProductUsageTemplateDict]
    price_point_overrides: list[WalletProductUsageTemplateDict]
    active_wallets: ActiveWalletsDict
