from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .currency_price import CurrencyPrice, CurrencyPriceDict
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .enums.price_point_type import PricePointTypeOrStr
from .enums.trial_type import TrialTypeOrStr


class ProductPricePoint(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    """The product price point name"""

    handle: OptionalNullable[str] = UNSET
    """The product price point API handle"""

    price_in_cents: Optional[int] = UNSET
    """The product price point price, in integer cents"""

    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this product
    price point would renew every 30 days."""

    interval_unit: Optional[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this product price point, either month or day"""

    trial_price_in_cents: OptionalNullable[int] = UNSET
    """The product price point trial price, in integer cents"""

    trial_interval: OptionalNullable[int] = UNSET
    """The numerical trial interval. e.g., an interval of ‘30’ coupled with a trial_interval_unit of day would mean this
    product price point trial would last 30 days."""

    trial_interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the trial interval unit for this product price point, either month or day"""

    trial_type: OptionalNullable[TrialTypeOrStr] = UNSET
    """Indicates how a trial is handled when the trial period ends and there is no credit card on file. For
    ``no_obligation``, the subscription transitions to a Trial Ended state. Maxio will not send any emails or
    statements. For ``payment_expected``, the subscription transitions to a Past Due state. Maxio will send normal
    dunning emails and statements according to your other settings."""

    introductory_offer: OptionalNullable[bool] = UNSET
    """reserved for future use"""

    initial_charge_in_cents: OptionalNullable[int] = UNSET
    """The product price point initial charge, in integer cents"""

    initial_charge_after_trial: OptionalNullable[bool] = UNSET
    expiration_interval: OptionalNullable[int] = UNSET
    """The numerical expiration interval. e.g., an expiration_interval of ‘30’ coupled with an expiration_interval_unit
    of day would mean this product price point would expire after 30 days."""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    """A string representing the expiration interval unit for this product price point, either month, day or never"""

    product_id: Optional[int] = UNSET
    """The product id this price point belongs to"""

    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp indicating when this price point was archived"""

    created_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when this price point was created"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when this price point was last updated"""

    use_site_exchange_rate: Optional[bool] = UNSET
    """Whether or not to use the site's exchange rate or define your own pricing when your site has multiple currencies
    defined."""

    type_: Optional[PricePointTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of price point"""

    tax_included: Optional[bool] = UNSET
    """Whether or not the price point includes tax"""

    subscription_id: OptionalNullable[int] = UNSET
    """The subscription id this price point belongs to"""

    currency_prices: Optional[list[CurrencyPrice]] = UNSET
    """An array of currency pricing data is available when multiple currencies are defined for the site. It varies based
    on the use_site_exchange_rate setting for the price point. This parameter is present only in the response of read
    endpoints, after including the appropriate query parameter."""


class ProductPricePointDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    handle: NotRequired[str | None]
    price_in_cents: NotRequired[int]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr]
    trial_price_in_cents: NotRequired[int | None]
    trial_interval: NotRequired[int | None]
    trial_interval_unit: NotRequired[IntervalUnitOrStr | None]
    trial_type: NotRequired[TrialTypeOrStr | None]
    introductory_offer: NotRequired[bool | None]
    initial_charge_in_cents: NotRequired[int | None]
    initial_charge_after_trial: NotRequired[bool | None]
    expiration_interval: NotRequired[int | None]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
    product_id: NotRequired[int]
    archived_at: NotRequired[RFC3339DateTime | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    use_site_exchange_rate: NotRequired[bool]
    type_: NotRequired[PricePointTypeOrStr]
    tax_included: NotRequired[bool]
    subscription_id: NotRequired[int | None]
    currency_prices: NotRequired[list[CurrencyPriceDict]]
