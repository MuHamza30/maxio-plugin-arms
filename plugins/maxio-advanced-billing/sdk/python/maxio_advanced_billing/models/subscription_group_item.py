from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SubscriptionGroupItem(SdkBaseModel):
    id: Optional[int] = UNSET
    reference: OptionalNullable[str] = UNSET
    product_id: Optional[int] = UNSET
    product_handle: OptionalNullable[str] = UNSET
    product_price_point_id: Optional[int] = UNSET
    product_price_point_handle: Optional[str] = UNSET
    currency: Optional[str] = UNSET
    coupon_code: OptionalNullable[str] = UNSET
    total_revenue_in_cents: Optional[int] = UNSET
    balance_in_cents: Optional[int] = UNSET


class SubscriptionGroupItemDict(TypedDict):
    id: NotRequired[int]
    reference: NotRequired[str | None]
    product_id: NotRequired[int]
    product_handle: NotRequired[str | None]
    product_price_point_id: NotRequired[int]
    product_price_point_handle: NotRequired[str]
    currency: NotRequired[str]
    coupon_code: NotRequired[str | None]
    total_revenue_in_cents: NotRequired[int]
    balance_in_cents: NotRequired[int]
