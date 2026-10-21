from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_coupon_currency import UpdateCouponCurrency, UpdateCouponCurrencyDict


class CouponCurrencyRequest(SdkBaseModel):
    currency_prices: list[UpdateCouponCurrency]


class CouponCurrencyRequestDict(TypedDict):
    currency_prices: list[UpdateCouponCurrencyDict]
