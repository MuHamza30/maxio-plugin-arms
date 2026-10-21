from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_subscription import CreateSubscription, CreateSubscriptionDict


class CreateSubscriptionRequest(SdkBaseModel):
    subscription: CreateSubscription


class CreateSubscriptionRequestDict(TypedDict):
    subscription: CreateSubscriptionDict
