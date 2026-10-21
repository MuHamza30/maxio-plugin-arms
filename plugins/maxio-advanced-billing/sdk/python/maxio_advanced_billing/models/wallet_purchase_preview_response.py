from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet_purchase_preview import WalletPurchasePreview, WalletPurchasePreviewDict


class WalletPurchasePreviewResponse(SdkBaseModel):
    wallet_purchase_previews: list[WalletPurchasePreview]


class WalletPurchasePreviewResponseDict(TypedDict):
    wallet_purchase_previews: list[WalletPurchasePreviewDict]
