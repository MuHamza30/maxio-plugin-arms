from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription import Subscription, SubscriptionDict


class SubscriptionResponse(SdkBaseModel):
    subscription: Optional[Subscription] = UNSET


class SubscriptionResponseDict(TypedDict):
    subscription: NotRequired[SubscriptionDict]
