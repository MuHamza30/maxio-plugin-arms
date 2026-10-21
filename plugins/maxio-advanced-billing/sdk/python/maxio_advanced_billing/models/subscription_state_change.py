from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubscriptionStateChange(SdkBaseModel):
    previous_subscription_state: str
    new_subscription_state: str


class SubscriptionStateChangeDict(TypedDict):
    previous_subscription_state: str
    new_subscription_state: str
