from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CouponCurrency(SdkBaseModel):
    id: OptionalNullable[int] = UNSET
    currency: Optional[str] = UNSET
    price: OptionalNullable[float] = UNSET
    coupon_id: Optional[int] = UNSET


class CouponCurrencyDict(TypedDict):
    id: NotRequired[int | None]
    currency: NotRequired[str]
    price: NotRequired[float | None]
    coupon_id: NotRequired[int]
