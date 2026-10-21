from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateCouponCurrency(SdkBaseModel):
    currency: str
    """ISO code for the site defined currency."""

    price: int
    """Price for the given currency."""


class UpdateCouponCurrencyDict(TypedDict):
    currency: str
    price: int
