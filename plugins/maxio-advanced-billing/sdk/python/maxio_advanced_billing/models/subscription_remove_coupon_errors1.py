from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubscriptionRemoveCouponErrors1(SdkBaseModel):
    subscription: list[str]


class SubscriptionRemoveCouponErrors1Dict(TypedDict):
    subscription: list[str]
