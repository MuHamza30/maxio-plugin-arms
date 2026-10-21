from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .enums.trial_type import TrialTypeOrStr


class CreateProductPricePoint(SdkBaseModel):
    name: str
    """The product price point name"""

    handle: Optional[str] = UNSET
    """The product price point API handle"""

    price_in_cents: int
    """The product price point price, in integer cents"""

    interval: int
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this product
    price point would renew every 30 days."""

    interval_unit: IntervalUnitOrStr
    """A string representing the interval unit for this product price point, either month or day"""

    trial_price_in_cents: Optional[int] = UNSET
    """The product price point trial price, in integer cents"""

    trial_interval: Optional[int] = UNSET
    """The numerical trial interval. e.g., an interval of ‘30’ coupled with a trial_interval_unit of day would mean this
    product price point trial would last 30 days."""

    trial_interval_unit: Optional[IntervalUnitOrStr] = UNSET
    """A string representing the trial interval unit for this product price point, either month or day"""

    trial_type: OptionalNullable[TrialTypeOrStr] = UNSET
    """Indicates how a trial is handled when the trial period ends and there is no credit card on file. For
    ``no_obligation``, the subscription transitions to a Trial Ended state. Maxio will not send any emails or
    statements. For ``payment_expected``, the subscription transitions to a Past Due state. Maxio will send normal
    dunning emails and statements according to your other settings."""

    initial_charge_in_cents: Optional[int] = UNSET
    """The product price point initial charge, in integer cents"""

    initial_charge_after_trial: Optional[bool] = UNSET
    expiration_interval: Optional[int] = UNSET
    """The numerical expiration interval. e.g., an expiration_interval of ‘30’ coupled with an expiration_interval_unit
    of day would mean this product price point would expire after 30 days."""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    """A string representing the expiration interval unit for this product price point, either month, day or never"""

    use_site_exchange_rate: bool = True
    """Whether or not to use the site's exchange rate or define your own pricing when your site has multiple currencies
    defined."""


class CreateProductPricePointDict(TypedDict):
    name: str
    handle: NotRequired[str]
    price_in_cents: int
    interval: int
    interval_unit: IntervalUnitOrStr
    trial_price_in_cents: NotRequired[int]
    trial_interval: NotRequired[int]
    trial_interval_unit: NotRequired[IntervalUnitOrStr]
    trial_type: NotRequired[TrialTypeOrStr | None]
    initial_charge_in_cents: NotRequired[int]
    initial_charge_after_trial: NotRequired[bool]
    expiration_interval: NotRequired[int]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
    use_site_exchange_rate: NotRequired[bool]
