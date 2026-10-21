from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.subscription_group_prepayment_method import SubscriptionGroupPrepaymentMethodOrStr


class SubscriptionGroupPrepayment(SdkBaseModel):
    amount: int
    details: str
    memo: str
    method: SubscriptionGroupPrepaymentMethodOrStr


class SubscriptionGroupPrepaymentDict(TypedDict):
    amount: int
    details: str
    memo: str
    method: SubscriptionGroupPrepaymentMethodOrStr
