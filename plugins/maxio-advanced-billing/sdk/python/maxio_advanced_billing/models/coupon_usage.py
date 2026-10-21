from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CouponUsage(SdkBaseModel):
    id: Optional[int] = UNSET
    """The Chargify id of the product"""

    name: Optional[str] = UNSET
    """Name of the product"""

    signups: Optional[int] = UNSET
    """Number of times the coupon has been applied"""

    savings: OptionalNullable[int] = UNSET
    """Dollar amount of customer savings as a result of the coupon."""

    savings_in_cents: OptionalNullable[int] = UNSET
    """Dollar amount of customer savings as a result of the coupon."""

    revenue: OptionalNullable[int] = UNSET
    """Total revenue of all subscriptions that have received a discount from this coupon."""

    revenue_in_cents: Optional[int] = UNSET
    """Total revenue of all subscriptions that have received a discount from this coupon."""


class CouponUsageDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    signups: NotRequired[int]
    savings: NotRequired[int | None]
    savings_in_cents: NotRequired[int | None]
    revenue: NotRequired[int | None]
    revenue_in_cents: NotRequired[int]
