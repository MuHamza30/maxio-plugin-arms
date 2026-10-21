from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_group_prepayment import SubscriptionGroupPrepayment, SubscriptionGroupPrepaymentDict


class SubscriptionGroupPrepaymentRequest(SdkBaseModel):
    prepayment: SubscriptionGroupPrepayment


class SubscriptionGroupPrepaymentRequestDict(TypedDict):
    prepayment: SubscriptionGroupPrepaymentDict
