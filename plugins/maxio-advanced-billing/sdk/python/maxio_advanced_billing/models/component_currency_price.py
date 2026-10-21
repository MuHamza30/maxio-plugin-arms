from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ComponentCurrencyPrice(SdkBaseModel):
    id: Optional[int] = UNSET
    currency: Optional[str] = UNSET
    price: Optional[str] = UNSET
    formatted_price: Optional[str] = UNSET
    price_id: Optional[int] = UNSET
    price_point_id: Optional[int] = UNSET


class ComponentCurrencyPriceDict(TypedDict):
    id: NotRequired[int]
    currency: NotRequired[str]
    price: NotRequired[str]
    formatted_price: NotRequired[str]
    price_id: NotRequired[int]
    price_point_id: NotRequired[int]
