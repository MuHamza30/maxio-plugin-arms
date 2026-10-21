from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.entitlement_periodicity_unit import EntitlementPeriodicityUnitOrStr
from .enums.feature_kind import FeatureKindOrStr
from .enums.feature_value_type import FeatureValueTypeOrStr


class FeatureTemplate(SdkBaseModel):
    """A feature that can be granted to subscribers, defined once at the site level and then attached to products or
    components."""

    id: Optional[int] = UNSET
    """The Advanced Billing id of the feature template."""

    key: Optional[str] = UNSET
    """A unique, lowercase, underscore-separated identifier for the feature. Immutable once set."""

    name: Optional[str] = UNSET
    """The display name of the feature."""

    description: OptionalNullable[str] = UNSET
    kind: Optional[FeatureKindOrStr] = UNSET
    """The behavior of a feature:
    - ``access_right``: a boolean entitlement. A subscriber either has access or does not.
    - ``usage_limit``: a quantified allowance measured over a recurring period (for example, "10,000 API calls per
        month").
    - ``service_right``: a free-form value (text, boolean, or number) that isn't a simple access flag or a metered
        limit."""

    unit: OptionalNullable[str] = UNSET
    """The unit the feature is measured in (for example, ``requests`` or ``GB``). Required when ``kind`` is
    ``usage_limit``."""

    value_type: Optional[FeatureValueTypeOrStr] = UNSET
    """The data type of a feature's value. For ``access_right`` features this is always ``boolean``, and for
    ``usage_limit`` features this is always ``numeric``. For ``service_right`` features, you choose the value type
    explicitly."""

    default_value: OptionalNullable[str] = UNSET
    """A default value used to pre-populate new feature catalog items created from this template."""

    default_periodicity_interval: OptionalNullable[int] = UNSET
    """For ``usage_limit`` features, the default periodicity interval used to pre-populate new feature catalog items.
    Always ``null`` for other kinds."""

    default_periodicity_unit: OptionalNullable[EntitlementPeriodicityUnitOrStr] = UNSET
    """For ``usage_limit`` features, the default periodicity unit used to pre-populate new feature catalog items. Always
    ``null`` for other kinds."""

    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The date and time the feature template was archived, or ``null`` if it is active."""

    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET
    products_count: Optional[int] = UNSET
    """The number of **components** this feature template is currently attached to via an active feature catalog item.
    Despite the name, this counts components, not products. In the Advanced Billing UI, components are labeled
    "Products."
    """

    plans_count: Optional[int] = UNSET
    """The number of **products** this feature template is currently attached to via an active feature catalog item.
    Despite the name, this counts products, not plans. In the Advanced Billing UI, products are labeled "Plans."
    """


class FeatureTemplateDict(TypedDict):
    id: NotRequired[int]
    key: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str | None]
    kind: NotRequired[FeatureKindOrStr]
    unit: NotRequired[str | None]
    value_type: NotRequired[FeatureValueTypeOrStr]
    default_value: NotRequired[str | None]
    default_periodicity_interval: NotRequired[int | None]
    default_periodicity_unit: NotRequired[EntitlementPeriodicityUnitOrStr | None]
    archived_at: NotRequired[RFC3339DateTime | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    products_count: NotRequired[int]
    plans_count: NotRequired[int]
