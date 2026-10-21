from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet2 import Wallet2, Wallet2Dict


class UpdateWalletRequest(SdkBaseModel):
    wallet: Wallet2


class UpdateWalletRequestDict(TypedDict):
    wallet: Wallet2Dict
