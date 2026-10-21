from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .unions.interval import Interval, IntervalDict
from .unions.price_in_cents import PriceInCents, PriceInCentsDict


class ScheduledRenewalProductPricePoint(SdkBaseModel):
    """Custom pricing for a product within a scheduled renewal."""

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

    tax_included: Optional[bool] = UNSET
    """(Optional)"""

    initial_charge_in_cents: Optional[int] = UNSET
    """The product price point initial charge, in integer cents."""

    expiration_interval: Optional[int] = UNSET
    """The numerical expiration interval. e.g., an expiration_interval of ‘30’ coupled with an expiration_interval_unit
    of day would mean this product price point would expire after 30 days."""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    """A string representing the expiration interval unit for this product price point, either month, day or never"""


class ScheduledRenewalProductPricePointDict(TypedDict):
    name: NotRequired[str]
    handle: NotRequired[str]
    price_in_cents: PriceInCentsDict
    interval: IntervalDict
    interval_unit: IntervalUnitOrStr | None
    tax_included: NotRequired[bool]
    initial_charge_in_cents: NotRequired[int]
    expiration_interval: NotRequired[int]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
