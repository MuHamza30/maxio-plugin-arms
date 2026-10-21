from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.entitlement_periodicity_unit import EntitlementPeriodicityUnitOrStr
from .enums.feature_kind import FeatureKindOrStr
from .enums.feature_owner_price_point_type import FeatureOwnerPricePointTypeOrStr


class FeatureCatalogItem(SdkBaseModel):
    """A feature template attached to a specific product or component (or one of their price points), with a concrete
    value. When a subscriber signs up for or is assigned this product/component, the feature catalog item is provisioned
    as an entitlement on their subscription."""

    id: Optional[int] = UNSET
    feature_template_id: Optional[int] = UNSET
    """The id of the feature template this item was created from."""

    feature_key: Optional[str] = UNSET
    """The ``key`` of the parent feature template."""

    feature_name: Optional[str] = UNSET
    """The ``name`` of the parent feature template."""

    feature_kind: Optional[FeatureKindOrStr] = UNSET
    """The behavior of a feature:
    - ``access_right``: a boolean entitlement. A subscriber either has access or does not.
    - ``usage_limit``: a quantified allowance measured over a recurring period (for example, "10,000 API calls per
        month").
    - ``service_right``: a free-form value (text, boolean, or number) that isn't a simple access flag or a metered
        limit."""

    value: Optional[str] = UNSET
    """The value granted by this feature catalog item. Interpreted according to ``feature_kind``: ``"true"``/``"false"``
    for ``access_right``, a numeric string for ``usage_limit``, or any string for ``service_right`` (shaped by the
    feature template's ``value_type``)."""

    periodicity_interval: OptionalNullable[int] = UNSET
    """Set when ``feature_kind`` is ``usage_limit``; ``null`` otherwise."""

    periodicity_unit: OptionalNullable[EntitlementPeriodicityUnitOrStr] = UNSET
    """Set when ``feature_kind`` is ``usage_limit``; ``null`` otherwise."""

    price_point_type: OptionalNullable[FeatureOwnerPricePointTypeOrStr] = UNSET
    """``null`` when this feature catalog item applies to every price point of its owning product/component. Set when
    the feature catalog item is an override for one specific price point."""

    price_point_id: OptionalNullable[int] = UNSET
    """Set together with ``price_point_type`` for price-point-specific overrides."""

    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET


class FeatureCatalogItemDict(TypedDict):
    id: NotRequired[int]
    feature_template_id: NotRequired[int]
    feature_key: NotRequired[str]
    feature_name: NotRequired[str]
    feature_kind: NotRequired[FeatureKindOrStr]
    value: NotRequired[str]
    periodicity_interval: NotRequired[int | None]
    periodicity_unit: NotRequired[EntitlementPeriodicityUnitOrStr | None]
    price_point_type: NotRequired[FeatureOwnerPricePointTypeOrStr | None]
    price_point_id: NotRequired[int | None]
    archived_at: NotRequired[RFC3339DateTime | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
