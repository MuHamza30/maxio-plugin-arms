from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.entitlement_periodicity_unit import EntitlementPeriodicityUnitOrStr
from .enums.feature_value_type import FeatureValueTypeOrStr


class Feature1(SdkBaseModel):
    """``key`` cannot be changed once set. ``kind`` cannot be changed once any feature catalog item has been created
    from this template."""

    name: Optional[str] = UNSET
    description: OptionalNullable[str] = UNSET
    unit: OptionalNullable[str] = UNSET
    value_type: Optional[FeatureValueTypeOrStr] = UNSET
    """The data type of a feature's value. For ``access_right`` features this is always ``boolean``, and for
    ``usage_limit`` features this is always ``numeric``. For ``service_right`` features, you choose the value type
    explicitly."""

    default_value: OptionalNullable[str] = UNSET
    default_periodicity_interval: OptionalNullable[int] = UNSET
    default_periodicity_unit: OptionalNullable[EntitlementPeriodicityUnitOrStr] = UNSET


class Feature1Dict(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str | None]
    unit: NotRequired[str | None]
    value_type: NotRequired[FeatureValueTypeOrStr]
    default_value: NotRequired[str | None]
    default_periodicity_interval: NotRequired[int | None]
    default_periodicity_unit: NotRequired[EntitlementPeriodicityUnitOrStr | None]
