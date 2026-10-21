from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .coupon_currency import CouponCurrency, CouponCurrencyDict


class CouponCurrencyResponse(SdkBaseModel):
    currency_prices: Optional[list[CouponCurrency]] = UNSET


class CouponCurrencyResponseDict(TypedDict):
    currency_prices: NotRequired[list[CouponCurrencyDict]]
