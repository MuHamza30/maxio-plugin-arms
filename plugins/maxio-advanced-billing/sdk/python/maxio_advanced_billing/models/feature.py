from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.entitlement_periodicity_unit import EntitlementPeriodicityUnitOrStr
from .enums.feature_kind import FeatureKindOrStr
from .enums.feature_value_type import FeatureValueTypeOrStr


class Feature(SdkBaseModel):
    key: str
    """A unique, lowercase, underscore-separated identifier for the feature. Immutable once set."""

    name: str
    """The display name of the feature."""

    description: OptionalNullable[str] = UNSET
    kind: FeatureKindOrStr
    """The behavior of a feature:
    - ``access_right``: a boolean entitlement. A subscriber either has access or does not.
    - ``usage_limit``: a quantified allowance measured over a recurring period (for example, "10,000 API calls per
        month").
    - ``service_right``: a free-form value (text, boolean, or number) that isn't a simple access flag or a metered
        limit."""

    unit: OptionalNullable[str] = UNSET
    """Required when ``kind`` is ``usage_limit``."""

    value_type: Optional[FeatureValueTypeOrStr] = UNSET
    """Required when ``kind`` is ``service_right``. Ignored for other kinds, where it is inferred automatically."""

    default_value: OptionalNullable[str] = UNSET
    default_periodicity_interval: OptionalNullable[int] = UNSET
    """Only valid when ``kind`` is ``usage_limit``."""

    default_periodicity_unit: OptionalNullable[EntitlementPeriodicityUnitOrStr] = UNSET
    """Only valid when ``kind`` is ``usage_limit``. Must be set together with ``default_periodicity_interval``."""


class FeatureDict(TypedDict):
    key: str
    name: str
    description: NotRequired[str | None]
    kind: FeatureKindOrStr
    unit: NotRequired[str | None]
    value_type: NotRequired[FeatureValueTypeOrStr]
    default_value: NotRequired[str | None]
    default_periodicity_interval: NotRequired[int | None]
    default_periodicity_unit: NotRequired[EntitlementPeriodicityUnitOrStr | None]
