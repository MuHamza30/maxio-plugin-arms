from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet_product import WalletProduct, WalletProductDict


class CreateWalletProductRequest(SdkBaseModel):
    """Does not accept ``product_family_id``: a Wallet Product never belongs to a product family. The underlying
    endpoint accepts the param, but only to reject it; sending one returns ``422`` ("Product family cannot be set on a
    wallet product") rather than silently ignoring it."""

    wallet_product: WalletProduct


class CreateWalletProductRequestDict(TypedDict):
    wallet_product: WalletProductDict
