from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.pricing_scheme import PricingSchemeOrStr
from .overage_pricing import OveragePricing, OveragePricingDict
from .price import Price, PriceDict


class CreatePrepaidUsageComponentPricePoint(SdkBaseModel):
    name: str
    handle: Optional[str] = UNSET
    pricing_scheme: PricingSchemeOrStr
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    prices: list[Price]
    overage_pricing: OveragePricing
    use_site_exchange_rate: bool = True
    """Whether to use the site level exchange rate or define your own prices for each currency if you have multiple
    currencies defined on the site."""

    rollover_prepaid_remainder: Optional[bool] = UNSET
    """(only for prepaid usage components) Boolean which controls whether or not remaining units should be rolled over
    to the next period."""

    renew_prepaid_allocation: Optional[bool] = UNSET
    """(only for prepaid usage components) Boolean which controls whether or not the allocated quantity should be
    renewed at the beginning of each period."""

    expiration_interval: Optional[float] = UNSET
    """(only for prepaid usage components where rollover_prepaid_remainder is true) The number of
    ``expiration_interval_unit``s after which rollover amounts should expire."""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    """(only for prepaid usage components where rollover_prepaid_remainder is true) A string representing the expiration
    interval unit for this component, either month or day."""


class CreatePrepaidUsageComponentPricePointDict(TypedDict):
    name: str
    handle: NotRequired[str]
    pricing_scheme: PricingSchemeOrStr
    prices: list[PriceDict]
    overage_pricing: OveragePricingDict
    use_site_exchange_rate: NotRequired[bool]
    rollover_prepaid_remainder: NotRequired[bool]
    renew_prepaid_allocation: NotRequired[bool]
    expiration_interval: NotRequired[float]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
