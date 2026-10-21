from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list_subscription_group_prepayment import ListSubscriptionGroupPrepayment, ListSubscriptionGroupPrepaymentDict


class ListSubscriptionGroupPrepaymentResponse(SdkBaseModel):
    prepayments: list[ListSubscriptionGroupPrepayment]


class ListSubscriptionGroupPrepaymentResponseDict(TypedDict):
    prepayments: list[ListSubscriptionGroupPrepaymentDict]
