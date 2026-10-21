from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.currency_price_role import CurrencyPriceRoleOrStr


class CurrencyPrice(SdkBaseModel):
    id: Optional[int] = UNSET
    currency: Optional[str] = UNSET
    price: Optional[float] = UNSET
    formatted_price: Optional[str] = UNSET
    price_id: Optional[int] = UNSET
    price_point_id: Optional[int] = UNSET
    product_price_point_id: Optional[int] = UNSET
    role: Optional[CurrencyPriceRoleOrStr] = UNSET
    """Role for the price."""


class CurrencyPriceDict(TypedDict):
    id: NotRequired[int]
    currency: NotRequired[str]
    price: NotRequired[float]
    formatted_price: NotRequired[str]
    price_id: NotRequired[int]
    price_point_id: NotRequired[int]
    product_price_point_id: NotRequired[int]
    role: NotRequired[CurrencyPriceRoleOrStr]
