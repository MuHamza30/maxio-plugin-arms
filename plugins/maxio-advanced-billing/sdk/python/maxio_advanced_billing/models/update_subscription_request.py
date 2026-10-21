from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_subscription import UpdateSubscription, UpdateSubscriptionDict


class UpdateSubscriptionRequest(SdkBaseModel):
    subscription: UpdateSubscription


class UpdateSubscriptionRequestDict(TypedDict):
    subscription: UpdateSubscriptionDict
