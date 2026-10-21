from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet_product1 import WalletProduct1, WalletProduct1Dict


class UpdateWalletProductRequest(SdkBaseModel):
    """Only ``name``, ``description``, ``taxable``, ``tax_code``, ``accounting_code``, and ``item_category`` are
    mutable. ``unit_name``, ``handle``, ``price_point``, and ``price_points`` are not accepted here: the request still
    returns ``200``, but those fields are silently ignored and nothing about them changes. ``handle`` stays fixed
    because it's the Wallet Product's only stable identifier on a surface with no product family in the path;
    ``unit_name`` stays fixed because a wallet's behavior snapshots it into the wallet's own ``unit`` field and never
    re-derives it."""

    wallet_product: WalletProduct1


class UpdateWalletProductRequestDict(TypedDict):
    wallet_product: WalletProduct1Dict
