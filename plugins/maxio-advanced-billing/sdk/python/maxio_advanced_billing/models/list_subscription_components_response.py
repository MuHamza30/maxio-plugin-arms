from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_component import SubscriptionComponent, SubscriptionComponentDict


class ListSubscriptionComponentsResponse(SdkBaseModel):
    subscriptions_components: list[SubscriptionComponent]


class ListSubscriptionComponentsResponseDict(TypedDict):
    subscriptions_components: list[SubscriptionComponentDict]
