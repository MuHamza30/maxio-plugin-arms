from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .enums.trial_type import TrialTypeOrStr
from .unions.expiration_interval import ExpirationInterval, ExpirationIntervalDict
from .unions.initial_charge_in_cents import InitialChargeInCents, InitialChargeInCentsDict
from .unions.interval import Interval, IntervalDict
from .unions.price_in_cents import PriceInCents, PriceInCentsDict
from .unions.trial_interval import TrialInterval, TrialIntervalDict
from .unions.trial_price_in_cents import TrialPriceInCents, TrialPriceInCentsDict


class SubscriptionCustomPrice(SdkBaseModel):
    """(Optional) Used in place of ``product_price_point_id`` to define a custom price point unique to the subscription.
    A subscription can have up to 30 custom price points. Exceeding this limit will result in an API error."""

    name: Optional[str] = UNSET
    """(Optional)"""

    handle: Optional[str] = UNSET
    """(Optional)"""

    price_in_cents: PriceInCents
    """Required if using ``custom_price`` attribute."""

    interval: Interval
    """Required if using ``custom_price`` attribute."""

    interval_unit: IntervalUnitOrStr | None
    """Required if using ``custom_price`` attribute."""

    trial_price_in_cents: Optional[TrialPriceInCents] = UNSET
    """(Optional)"""

    trial_interval: Optional[TrialInterval] = UNSET
    """(Optional)"""

    trial_interval_unit: Optional[IntervalUnitOrStr] = UNSET
    """(Optional)"""

    trial_type: OptionalNullable[TrialTypeOrStr] = UNSET
    """Indicates how a trial is handled when the trial period ends and there is no credit card on file. For
    ``no_obligation``, the subscription transitions to a Trial Ended state. Maxio will not send any emails or
    statements. For ``payment_expected``, the subscription transitions to a Past Due state. Maxio will send normal
    dunning emails and statements according to your other settings."""

    initial_charge_in_cents: Optional[InitialChargeInCents] = UNSET
    """(Optional)"""

    initial_charge_after_trial: Optional[bool] = UNSET
    """(Optional)"""

    expiration_interval: Optional[ExpirationInterval] = UNSET
    """(Optional)"""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    """(Optional)"""

    tax_included: Optional[bool] = UNSET
    """(Optional)"""


class SubscriptionCustomPriceDict(TypedDict):
    name: NotRequired[str]
    handle: NotRequired[str]
    price_in_cents: PriceInCentsDict
    interval: IntervalDict
    interval_unit: IntervalUnitOrStr | None
    trial_price_in_cents: NotRequired[TrialPriceInCentsDict]
    trial_interval: NotRequired[TrialIntervalDict]
    trial_interval_unit: NotRequired[IntervalUnitOrStr]
    trial_type: NotRequired[TrialTypeOrStr | None]
    initial_charge_in_cents: NotRequired[InitialChargeInCentsDict]
    initial_charge_after_trial: NotRequired[bool]
    expiration_interval: NotRequired[ExpirationIntervalDict]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
    tax_included: NotRequired[bool]
