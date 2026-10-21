from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_group_signup_error import SubscriptionGroupSignupError, SubscriptionGroupSignupErrorDict


class SubscriptionGroupSignupErrorResponse1(SdkBaseModel):
    errors: SubscriptionGroupSignupError


class SubscriptionGroupSignupErrorResponse1Dict(TypedDict):
    errors: SubscriptionGroupSignupErrorDict
