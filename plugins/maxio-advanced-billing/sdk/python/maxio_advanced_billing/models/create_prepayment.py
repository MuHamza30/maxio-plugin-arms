from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.create_prepayment_method import CreatePrepaymentMethodOrStr


class CreatePrepayment(SdkBaseModel):
    amount: float
    details: str
    memo: str
    method: CreatePrepaymentMethodOrStr
    """When the ``method`` specified is ``"credit_card_on_file"``, the prepayment amount will be collected using the
    default credit card payment profile and applied to the prepayment account balance. This is especially useful for
    manual replenishment of prepaid subscriptions."""

    payment_profile_id: Optional[int] = UNSET


class CreatePrepaymentDict(TypedDict):
    amount: float
    details: str
    memo: str
    method: CreatePrepaymentMethodOrStr
    payment_profile_id: NotRequired[int]
