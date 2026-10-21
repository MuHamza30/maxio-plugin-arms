from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_group import SubscriptionGroup, SubscriptionGroupDict


class SubscriptionGroupResponse(SdkBaseModel):
    subscription_group: SubscriptionGroup


class SubscriptionGroupResponseDict(TypedDict):
    subscription_group: SubscriptionGroupDict
