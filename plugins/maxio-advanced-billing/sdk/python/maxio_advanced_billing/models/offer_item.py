from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .currency_price import CurrencyPrice, CurrencyPriceDict
from .enums.interval_unit import IntervalUnitOrStr


class OfferItem(SdkBaseModel):
    component_id: Optional[int] = UNSET
    price_point_id: Optional[int] = UNSET
    starting_quantity: Optional[str] = UNSET
    editable: Optional[bool] = UNSET
    component_unit_price: Optional[str] = UNSET
    component_name: Optional[str] = UNSET
    price_point_name: Optional[str] = UNSET
    currency_prices: Optional[list[CurrencyPrice]] = UNSET
    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of '30' coupled with an interval_unit of day would mean this component
    price point would renew every 30 days. This property is only available for sites with Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this component price point, either month or day. This property is
    only available for sites with Multifrequency enabled."""


class OfferItemDict(TypedDict):
    component_id: NotRequired[int]
    price_point_id: NotRequired[int]
    starting_quantity: NotRequired[str]
    editable: NotRequired[bool]
    component_unit_price: NotRequired[str]
    component_name: NotRequired[str]
    price_point_name: NotRequired[str]
    currency_prices: NotRequired[list[CurrencyPriceDict]]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
