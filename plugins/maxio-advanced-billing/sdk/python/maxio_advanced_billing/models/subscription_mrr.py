from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription_mrr_breakout import SubscriptionMrrBreakout, SubscriptionMrrBreakoutDict


class SubscriptionMrr(SdkBaseModel):
    subscription_id: int
    mrr_amount_in_cents: int
    breakouts: Optional[SubscriptionMrrBreakout] = UNSET


class SubscriptionMrrDict(TypedDict):
    subscription_id: int
    mrr_amount_in_cents: int
    breakouts: NotRequired[SubscriptionMrrBreakoutDict]
