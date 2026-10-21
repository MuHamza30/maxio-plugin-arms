from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_subscription_group import CreateSubscriptionGroup, CreateSubscriptionGroupDict


class CreateSubscriptionGroupRequest(SdkBaseModel):
    subscription_group: CreateSubscriptionGroup


class CreateSubscriptionGroupRequestDict(TypedDict):
    subscription_group: CreateSubscriptionGroupDict
