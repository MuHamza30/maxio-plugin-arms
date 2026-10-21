from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.entitlement_periodicity_unit import EntitlementPeriodicityUnitOrStr


class AggregatedEntitlementPeriodicity(SdkBaseModel):
    interval: Optional[int] = UNSET
    unit: Optional[EntitlementPeriodicityUnitOrStr] = UNSET
    """The recurring window over which a ``usage_limit`` feature's allowance resets."""


class AggregatedEntitlementPeriodicityDict(TypedDict):
    interval: NotRequired[int]
    unit: NotRequired[EntitlementPeriodicityUnitOrStr]
