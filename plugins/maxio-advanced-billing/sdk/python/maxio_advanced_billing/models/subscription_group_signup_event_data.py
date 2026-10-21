from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .customer import Customer, CustomerDict
from .subscription_group_signup_failure_data import (
    SubscriptionGroupSignupFailureData,
    SubscriptionGroupSignupFailureDataDict,
)


class SubscriptionGroupSignupEventData(SdkBaseModel):
    subscription_group: SubscriptionGroupSignupFailureData
    customer: Customer | None


class SubscriptionGroupSignupEventDataDict(TypedDict):
    subscription_group: SubscriptionGroupSignupFailureDataDict
    customer: CustomerDict | None
