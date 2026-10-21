from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_group_signup import SubscriptionGroupSignup, SubscriptionGroupSignupDict


class SubscriptionGroupSignupRequest(SdkBaseModel):
    subscription_group: SubscriptionGroupSignup


class SubscriptionGroupSignupRequestDict(TypedDict):
    subscription_group: SubscriptionGroupSignupDict
