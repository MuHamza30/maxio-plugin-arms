from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .component_currency_price import ComponentCurrencyPrice, ComponentCurrencyPriceDict
from .component_price import ComponentPrice, ComponentPriceDict
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .enums.price_point_type import PricePointTypeOrStr
from .enums.pricing_scheme import PricingSchemeOrStr


class ComponentPricePoint(SdkBaseModel):
    id: Optional[int] = UNSET
    type_: Optional[PricePointTypeOrStr] = Field(default=UNSET, alias="type")
    """Price point type. We expose the following types:
    1. **default**: a price point that is marked as a default price for a certain product.
    2. **custom**: a custom price point.
    3. **catalog**: a price point that is **not** marked as a default price for a certain product and is **not** a
        custom one."""

    default: Optional[bool] = UNSET
    """Note: Refer to type attribute instead."""

    name: Optional[str] = UNSET
    pricing_scheme: Optional[PricingSchemeOrStr] = UNSET
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    component_id: Optional[int] = UNSET
    handle: OptionalNullable[str] = UNSET
    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET
    prices: Optional[list[ComponentPrice]] = UNSET
    use_site_exchange_rate: Optional[bool] = UNSET
    """Whether to use the site level exchange rate or define your own prices for each currency if you have multiple
    currencies defined on the site. Defaults to true during creation."""

    subscription_id: Optional[int] = UNSET
    """(only used for Custom Pricing - ie. when the price point's type is ``custom``) The id of the subscription that
    the custom price point is for."""

    tax_included: Optional[bool] = UNSET
    interval: OptionalNullable[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this component
    price point would renew every 30 days. This property is only available for sites with Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this component price point, either month or day. This property is
    only available for sites with Multifrequency enabled."""

    currency_prices: Optional[list[ComponentCurrencyPrice]] = UNSET
    """An array of currency pricing data is available when multiple currencies are defined for the site. It varies based
    on the use_site_exchange_rate setting for the price point. This parameter is present only in the response of read
    endpoints, after including the appropriate query parameter. The clone endpoint always returns currency prices if
    they are present."""

    overage_prices: Optional[list[ComponentPrice]] = UNSET
    """Applicable only to prepaid usage components. An array of overage price brackets."""

    overage_pricing_scheme: Optional[PricingSchemeOrStr] = UNSET
    """Applicable only to prepaid usage components. Pricing scheme for overage pricing."""

    renew_prepaid_allocation: Optional[bool] = UNSET
    """Applicable only to prepaid usage components. Boolean which controls whether or not the allocated quantity should
    be renewed at the beginning of each period."""

    rollover_prepaid_remainder: Optional[bool] = UNSET
    """Applicable only to prepaid usage components. Boolean which controls whether or not remaining units should be
    rolled over to the next period."""

    expiration_interval: OptionalNullable[int] = UNSET
    """Applicable only to prepaid usage components where rollover_prepaid_remainder is true. The number of
    ``expiration_interval_unit``s after which rollover amounts should expire."""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    """Applicable only to prepaid usage components where rollover_prepaid_remainder is true. A string representing the
    expiration interval unit for this component, either month or day."""


class ComponentPricePointDict(TypedDict):
    id: NotRequired[int]
    type_: NotRequired[PricePointTypeOrStr]
    default: NotRequired[bool]
    name: NotRequired[str]
    pricing_scheme: NotRequired[PricingSchemeOrStr]
    component_id: NotRequired[int]
    handle: NotRequired[str | None]
    archived_at: NotRequired[RFC3339DateTime | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    prices: NotRequired[list[ComponentPriceDict]]
    use_site_exchange_rate: NotRequired[bool]
    subscription_id: NotRequired[int]
    tax_included: NotRequired[bool]
    interval: NotRequired[int | None]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
    currency_prices: NotRequired[list[ComponentCurrencyPriceDict]]
    overage_prices: NotRequired[list[ComponentPriceDict]]
    overage_pricing_scheme: NotRequired[PricingSchemeOrStr]
    renew_prepaid_allocation: NotRequired[bool]
    rollover_prepaid_remainder: NotRequired[bool]
    expiration_interval: NotRequired[int | None]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
