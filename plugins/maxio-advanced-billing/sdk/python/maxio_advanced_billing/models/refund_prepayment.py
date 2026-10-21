from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.amount5 import Amount5, Amount5Dict


class RefundPrepayment(SdkBaseModel):
    amount_in_cents: int | None
    """``amount`` is not required if you pass ``amount_in_cents``."""

    amount: Amount5
    """``amount_in_cents`` is not required if you pass ``amount``."""

    memo: str
    external: Optional[bool] = UNSET
    """Specify the type of refund you wish to initiate. When the prepayment is external, the ``external`` flag is
    optional. But if the prepayment was made through a payment profile, the ``external`` flag is required."""


class RefundPrepaymentDict(TypedDict):
    amount_in_cents: int | None
    amount: Amount5Dict
    memo: str
    external: NotRequired[bool]
