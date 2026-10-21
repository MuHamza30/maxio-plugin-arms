from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .component import Component, ComponentDict


class WalletProductResponse(SdkBaseModel):
    """A Wallet Product is a Component created with no product family, so it returns the full Component field set under
    a ``wallet_product`` root instead of ``component``."""

    wallet_product: Component


class WalletProductResponseDict(TypedDict):
    wallet_product: ComponentDict
