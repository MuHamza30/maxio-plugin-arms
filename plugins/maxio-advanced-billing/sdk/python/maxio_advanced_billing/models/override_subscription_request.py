from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .override_subscription import OverrideSubscription, OverrideSubscriptionDict


class OverrideSubscriptionRequest(SdkBaseModel):
    subscription: OverrideSubscription


class OverrideSubscriptionRequestDict(TypedDict):
    subscription: OverrideSubscriptionDict
