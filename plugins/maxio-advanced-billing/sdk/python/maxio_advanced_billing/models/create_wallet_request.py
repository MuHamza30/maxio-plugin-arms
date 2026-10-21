from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet1 import Wallet1, Wallet1Dict


class CreateWalletRequest(SdkBaseModel):
    wallet: Wallet1


class CreateWalletRequestDict(TypedDict):
    wallet: Wallet1Dict
