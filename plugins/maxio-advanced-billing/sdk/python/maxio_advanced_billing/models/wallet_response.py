from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet import Wallet, WalletDict


class WalletResponse(SdkBaseModel):
    wallet: Wallet
    """A balance, denominated in the unit of a Wallet Product, owned by a subscription. Grants and recurring funding
    schedules are embedded so a single read shows the full balance breakdown."""


class WalletResponseDict(TypedDict):
    wallet: WalletDict
