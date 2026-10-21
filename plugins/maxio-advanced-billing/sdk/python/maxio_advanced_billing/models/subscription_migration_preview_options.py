from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .proration import Proration, ProrationDict


class SubscriptionMigrationPreviewOptions(SdkBaseModel):
    product_id: Optional[int] = UNSET
    """The ID of the target Product. Either a product_id or product_handle must be present. A Subscription can be
    migrated to another product for both the current Product Family and another Product Family. Note: Going to another
    Product Family, components will not be migrated as well."""

    product_price_point_id: Optional[int] = UNSET
    """The ID of the specified product's price point. This can be passed to migrate to a non-default price point."""

    include_trial: bool = False
    """Whether to include the trial period configured for the product price point when starting a new billing period.
    Note that if preserve_period is set, then include_trial will be ignored."""

    include_initial_charge: bool = False
    """If ``true`` is sent initial charges will be assessed."""

    include_coupons: bool = True
    """If ``true`` is sent, any coupons associated with the subscription will be applied to the migration. If ``false``
    is sent, coupons will not be applied. Note: When migrating to a new product family, the coupon cannot migrate."""

    preserve_period: bool = False
    """If ``false`` is sent, the subscription's billing period will be reset to today and the full price of the new
    product will be charged. If ``true`` is sent, the billing period will not change and a prorated charge will be
    issued for the new product."""

    product_handle: Optional[str] = UNSET
    """The handle of the target Product. Either a product_id or product_handle must be present. A Subscription can be
    migrated to another product for both the current Product Family and another Product Family. Note: Going to another
    Product Family, components will not be migrated as well."""

    product_price_point_handle: Optional[str] = UNSET
    """The ID or handle of the specified product's price point. This can be passed to migrate to a non-default price
    point."""

    proration: Optional[Proration] = UNSET
    proration_date: Optional[RFC3339DateTime] = UNSET
    """The date that the proration is calculated from for the preview"""


class SubscriptionMigrationPreviewOptionsDict(TypedDict):
    product_id: NotRequired[int]
    product_price_point_id: NotRequired[int]
    include_trial: NotRequired[bool]
    include_initial_charge: NotRequired[bool]
    include_coupons: NotRequired[bool]
    preserve_period: NotRequired[bool]
    product_handle: NotRequired[str]
    product_price_point_handle: NotRequired[str]
    proration: NotRequired[ProrationDict]
    proration_date: NotRequired[RFC3339DateTime]
