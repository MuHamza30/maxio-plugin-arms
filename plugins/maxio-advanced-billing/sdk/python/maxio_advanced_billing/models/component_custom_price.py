from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .enums.pricing_scheme import PricingSchemeOrStr
from .price import Price, PriceDict


class ComponentCustomPrice(SdkBaseModel):
    """Create or update custom pricing unique to the subscription. Used in place of ``price_point_id``."""

    tax_included: Optional[bool] = UNSET
    """Whether or not the price point includes tax"""

    pricing_scheme: Optional[PricingSchemeOrStr] = UNSET
    """Omit for On/Off components."""

    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this component
    price point would renew every 30 days. This property is only available for sites with Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this component price point, either month or day. This property is
    only available for sites with Multifrequency enabled."""

    list_price_point_id: OptionalNullable[int] = UNSET
    """(Optional) Id of the price point to use for list price calculations when overriding the customer price."""

    use_default_list_price: Optional[bool] = UNSET
    """When true, list price calculations will continue to use the default price point even when a ``custom_price`` is
    supplied."""

    prices: list[Price]
    """On/off components only need one price bracket starting at 1."""

    renew_prepaid_allocation: Optional[bool] = UNSET
    """Applicable only to prepaid usage components. Controls whether the allocated quantity renews each period."""

    rollover_prepaid_remainder: Optional[bool] = UNSET
    """Applicable only to prepaid usage components. Controls whether remaining units roll over to the next period."""

    expiration_interval: OptionalNullable[int] = UNSET
    """Applicable only when rollover is enabled. Number of ``expiration_interval_unit``s after which rollover amounts
    expire."""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    """Applicable only when rollover is enabled. Interval unit for rollover expiration (month or day)."""


class ComponentCustomPriceDict(TypedDict):
    tax_included: NotRequired[bool]
    pricing_scheme: NotRequired[PricingSchemeOrStr]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
    list_price_point_id: NotRequired[int | None]
    use_default_list_price: NotRequired[bool]
    prices: list[PriceDict]
    renew_prepaid_allocation: NotRequired[bool]
    rollover_prepaid_remainder: NotRequired[bool]
    expiration_interval: NotRequired[int | None]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
