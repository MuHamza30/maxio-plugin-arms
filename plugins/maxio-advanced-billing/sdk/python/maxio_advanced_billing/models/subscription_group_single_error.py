from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubscriptionGroupSingleError(SdkBaseModel):
    subscription_group: str


class SubscriptionGroupSingleErrorDict(TypedDict):
    subscription_group: str
