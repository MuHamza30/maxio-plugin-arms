from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SubscriptionProductChange(SdkBaseModel):
    """Event data for both ``subscription_product_change`` and ``subscription_product_change_scheduled``. The price
    point and ``effective_at`` fields are only populated for scheduled changes."""

    previous_product_id: int
    new_product_id: int
    previous_product_price_point_id: OptionalNullable[int] = UNSET
    new_product_price_point_id: OptionalNullable[int] = UNSET
    effective_at: OptionalNullable[RFC3339DateTime] = UNSET
    """When the scheduled product change takes effect (the subscription's next renewal). Only sent for
    ``subscription_product_change_scheduled``."""


class SubscriptionProductChangeDict(TypedDict):
    previous_product_id: int
    new_product_id: int
    previous_product_price_point_id: NotRequired[int | None]
    new_product_price_point_id: NotRequired[int | None]
    effective_at: NotRequired[RFC3339DateTime | None]
