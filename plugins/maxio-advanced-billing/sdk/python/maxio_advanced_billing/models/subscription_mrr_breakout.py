from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubscriptionMrrBreakout(SdkBaseModel):
    plan_amount_in_cents: int
    usage_amount_in_cents: int


class SubscriptionMrrBreakoutDict(TypedDict):
    plan_amount_in_cents: int
    usage_amount_in_cents: int
