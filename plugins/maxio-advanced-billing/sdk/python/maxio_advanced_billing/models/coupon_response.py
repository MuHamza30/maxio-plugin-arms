from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .coupon import Coupon, CouponDict


class CouponResponse(SdkBaseModel):
    coupon: Optional[Coupon] = UNSET


class CouponResponseDict(TypedDict):
    coupon: NotRequired[CouponDict]
