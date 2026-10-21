from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list_subscription_group_prepayment_item import (
    ListSubscriptionGroupPrepaymentItem,
    ListSubscriptionGroupPrepaymentItemDict,
)


class ListSubscriptionGroupPrepayment(SdkBaseModel):
    prepayment: ListSubscriptionGroupPrepaymentItem


class ListSubscriptionGroupPrepaymentDict(TypedDict):
    prepayment: ListSubscriptionGroupPrepaymentItemDict
