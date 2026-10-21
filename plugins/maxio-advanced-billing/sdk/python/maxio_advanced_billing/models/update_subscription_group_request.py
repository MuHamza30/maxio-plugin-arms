from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_subscription_group import UpdateSubscriptionGroup, UpdateSubscriptionGroupDict


class UpdateSubscriptionGroupRequest(SdkBaseModel):
    subscription_group: UpdateSubscriptionGroup


class UpdateSubscriptionGroupRequestDict(TypedDict):
    subscription_group: UpdateSubscriptionGroupDict
