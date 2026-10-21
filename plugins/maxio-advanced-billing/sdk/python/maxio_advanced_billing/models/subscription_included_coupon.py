from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SubscriptionIncludedCoupon(SdkBaseModel):
    code: Optional[str] = UNSET
    use_count: Optional[int] = UNSET
    uses_allowed: Optional[int] = UNSET
    expires_at: OptionalNullable[str] = UNSET
    recurring: Optional[bool] = UNSET
    amount_in_cents: OptionalNullable[int] = UNSET
    percentage: OptionalNullable[str] = UNSET


class SubscriptionIncludedCouponDict(TypedDict):
    code: NotRequired[str]
    use_count: NotRequired[int]
    uses_allowed: NotRequired[int]
    expires_at: NotRequired[str | None]
    recurring: NotRequired[bool]
    amount_in_cents: NotRequired[int | None]
    percentage: NotRequired[str | None]
