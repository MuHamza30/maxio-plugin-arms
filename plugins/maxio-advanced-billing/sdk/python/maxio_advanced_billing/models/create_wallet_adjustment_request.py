from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .adjustment import Adjustment, AdjustmentDict


class CreateWalletAdjustmentRequest(SdkBaseModel):
    """A signed correction to a specific grant's balance, or to an overdraft entry's usage, intended for support and ops
    use."""

    adjustment: Adjustment


class CreateWalletAdjustmentRequestDict(TypedDict):
    adjustment: AdjustmentDict
