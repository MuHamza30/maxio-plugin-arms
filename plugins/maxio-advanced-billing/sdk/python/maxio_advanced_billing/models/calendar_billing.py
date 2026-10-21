from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.first_charge_type import FirstChargeTypeOrStr
from .unions.snap_day import SnapDay, SnapDayDict


class CalendarBilling(SdkBaseModel):
    """(Optional). Cannot be used when also specifying next_billing_at."""

    snap_day: Optional[SnapDay] = UNSET
    """A day of month that subscription will be processed on. Can be 1 up to 28 or 'end'."""

    calendar_billing_first_charge: Optional[FirstChargeTypeOrStr] = UNSET


class CalendarBillingDict(TypedDict):
    snap_day: NotRequired[SnapDayDict]
    calendar_billing_first_charge: NotRequired[FirstChargeTypeOrStr]
