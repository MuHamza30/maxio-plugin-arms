from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.interval_unit import IntervalUnitOrStr
from .enums.pricing_scheme import PricingSchemeOrStr
from .price import Price, PriceDict


class CreateComponentPricePoint(SdkBaseModel):
    name: str
    handle: Optional[str] = UNSET
    pricing_scheme: PricingSchemeOrStr
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    prices: list[Price]
    use_site_exchange_rate: bool = True
    """Whether to use the site level exchange rate or define your own prices for each currency if you have multiple
    currencies defined on the site. Setting not supported when creating price points in bulk."""

    tax_included: Optional[bool] = UNSET
    """Whether or not the price point includes tax. Setting not supported when creating price points in bulk."""

    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this price
    point would renew every 30 days. This property is only available for sites with Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this price point, either month or day. This property is only
    available for sites with Multifrequency enabled."""


class CreateComponentPricePointDict(TypedDict):
    name: str
    handle: NotRequired[str]
    pricing_scheme: PricingSchemeOrStr
    prices: list[PriceDict]
    use_site_exchange_rate: NotRequired[bool]
    tax_included: NotRequired[bool]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
