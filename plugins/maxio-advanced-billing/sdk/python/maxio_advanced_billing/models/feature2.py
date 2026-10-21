from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.entitlement_periodicity_unit import EntitlementPeriodicityUnitOrStr
from .enums.feature_owner_price_point_type import FeatureOwnerPricePointTypeOrStr


class Feature2(SdkBaseModel):
    feature_template_id: int
    """The id of the feature template to attach."""

    value: str
    periodicity_interval: OptionalNullable[int] = UNSET
    periodicity_unit: OptionalNullable[EntitlementPeriodicityUnitOrStr] = UNSET
    price_point_type: OptionalNullable[FeatureOwnerPricePointTypeOrStr] = UNSET
    """Omit to have this feature catalog item apply to every price point of the product/component. Set together with
    ``price_point_id`` to scope the feature catalog item to a single price point."""

    price_point_id: OptionalNullable[int] = UNSET
    propagate_to_subscriptions: bool = False
    """When ``true``, existing subscriptions on this product/component are immediately granted an entitlement for this
    feature, instead of waiting for their next subscription change."""


class Feature2Dict(TypedDict):
    feature_template_id: int
    value: str
    periodicity_interval: NotRequired[int | None]
    periodicity_unit: NotRequired[EntitlementPeriodicityUnitOrStr | None]
    price_point_type: NotRequired[FeatureOwnerPricePointTypeOrStr | None]
    price_point_id: NotRequired[int | None]
    propagate_to_subscriptions: NotRequired[bool]
