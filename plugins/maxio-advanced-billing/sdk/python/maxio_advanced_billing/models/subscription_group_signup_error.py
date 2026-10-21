from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payer_error import PayerError, PayerErrorDict
from .subscription_group_subscription_error import (
    SubscriptionGroupSubscriptionError,
    SubscriptionGroupSubscriptionErrorDict,
)


class SubscriptionGroupSignupError(SdkBaseModel):
    subscriptions: Optional[dict[str, SubscriptionGroupSubscriptionError]] = UNSET
    """Object that as key have subscription position in request subscriptions array and as value subscription errors
    object."""

    payer_reference: Optional[str] = UNSET
    payer: Optional[PayerError] = UNSET
    subscription_group: Optional[list[str]] = UNSET
    payment_profile_id: Optional[str] = UNSET
    payer_id: Optional[str] = UNSET


class SubscriptionGroupSignupErrorDict(TypedDict):
    subscriptions: NotRequired[dict[str, SubscriptionGroupSubscriptionErrorDict]]
    payer_reference: NotRequired[str]
    payer: NotRequired[PayerErrorDict]
    subscription_group: NotRequired[list[str]]
    payment_profile_id: NotRequired[str]
    payer_id: NotRequired[str]
