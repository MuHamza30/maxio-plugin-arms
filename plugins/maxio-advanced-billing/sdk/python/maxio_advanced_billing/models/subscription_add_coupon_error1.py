from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubscriptionAddCouponError1(SdkBaseModel):
    codes: Optional[list[str]] = UNSET
    coupon_code: Optional[list[str]] = UNSET
    coupon_codes: Optional[list[str]] = UNSET
    subscription: Optional[list[str]] = UNSET


class SubscriptionAddCouponError1Dict(TypedDict):
    codes: NotRequired[list[str]]
    coupon_code: NotRequired[list[str]]
    coupon_codes: NotRequired[list[str]]
    subscription: NotRequired[list[str]]
