from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_mrr import SubscriptionMrr, SubscriptionMrrDict


class SubscriptionMrrResponse(SdkBaseModel):
    subscriptions_mrr: list[SubscriptionMrr]


class SubscriptionMrrResponseDict(TypedDict):
    subscriptions_mrr: list[SubscriptionMrrDict]
