from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.entitlement_periodicity_unit import EntitlementPeriodicityUnitOrStr


class Feature3(SdkBaseModel):
    value: Optional[str] = UNSET
    periodicity_interval: OptionalNullable[int] = UNSET
    periodicity_unit: OptionalNullable[EntitlementPeriodicityUnitOrStr] = UNSET
    propagate_to_subscriptions: bool = False
    """When ``true``, the new ``value``/periodicity is immediately applied to every existing entitlement created from
    this feature catalog item."""


class Feature3Dict(TypedDict):
    value: NotRequired[str]
    periodicity_interval: NotRequired[int | None]
    periodicity_unit: NotRequired[EntitlementPeriodicityUnitOrStr | None]
    propagate_to_subscriptions: NotRequired[bool]
