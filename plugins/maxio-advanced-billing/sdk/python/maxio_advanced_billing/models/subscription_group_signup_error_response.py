from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_group_signup_error import SubscriptionGroupSignupError, SubscriptionGroupSignupErrorDict


class SubscriptionGroupSignupErrorResponse(SdkBaseModel):
    errors: SubscriptionGroupSignupError


class SubscriptionGroupSignupErrorResponseDict(TypedDict):
    errors: SubscriptionGroupSignupErrorDict
