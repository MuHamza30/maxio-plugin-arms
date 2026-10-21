from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.currency_price_role import CurrencyPriceRoleOrStr


class CreateProductCurrencyPrice(SdkBaseModel):
    currency: str
    """ISO code for one of the site level currencies."""

    price: int
    """Price for the given role."""

    role: CurrencyPriceRoleOrStr
    """Role for the price."""


class CreateProductCurrencyPriceDict(TypedDict):
    currency: str
    price: int
    role: CurrencyPriceRoleOrStr
