from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OfferDiscount(SdkBaseModel):
    coupon_code: Optional[str] = UNSET
    coupon_id: Optional[int] = UNSET
    coupon_name: Optional[str] = UNSET


class OfferDiscountDict(TypedDict):
    coupon_code: NotRequired[str]
    coupon_id: NotRequired[int]
    coupon_name: NotRequired[str]
