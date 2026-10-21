from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.interval_unit import IntervalUnitOrStr
from .enums.pricing_scheme import PricingSchemeOrStr
from .update_price import UpdatePrice, UpdatePriceDict


class UpdateComponentPricePoint(SdkBaseModel):
    name: Optional[str] = UNSET
    handle: Optional[str] = UNSET
    pricing_scheme: Optional[PricingSchemeOrStr] = UNSET
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    use_site_exchange_rate: Optional[bool] = UNSET
    """Whether to use the site level exchange rate or define your own prices for each currency if you have multiple
    currencies defined on the site."""

    tax_included: Optional[bool] = UNSET
    """Whether or not the price point includes tax"""

    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this component
    price point would renew every 30 days. This property is only available for sites with Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this component price point, either month or day. This property is
    only available for sites with Multifrequency enabled."""

    prices: Optional[list[UpdatePrice]] = UNSET


class UpdateComponentPricePointDict(TypedDict):
    name: NotRequired[str]
    handle: NotRequired[str]
    pricing_scheme: NotRequired[PricingSchemeOrStr]
    use_site_exchange_rate: NotRequired[bool]
    tax_included: NotRequired[bool]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
    prices: NotRequired[list[UpdatePriceDict]]
