from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .coupon_currency import CouponCurrency, CouponCurrencyDict
from .coupon_restriction import CouponRestriction, CouponRestrictionDict
from .enums.compounding_strategy import CompoundingStrategyOrStr
from .enums.discount_type import DiscountTypeOrStr
from .enums.recurring_scheme import RecurringSchemeOrStr


class Coupon(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    code: Optional[str] = UNSET
    description: Optional[str] = UNSET
    amount: OptionalNullable[float] = UNSET
    amount_in_cents: OptionalNullable[int] = UNSET
    product_family_id: Optional[int] = UNSET
    product_family_name: OptionalNullable[str] = UNSET
    start_date: Optional[RFC3339DateTime] = UNSET
    end_date: OptionalNullable[RFC3339DateTime] = UNSET
    """After the given time, this coupon code will be invalid for new signups. Recurring discounts started before this
    date will continue to recur even after this date."""

    percentage: OptionalNullable[str] = UNSET
    recurring: Optional[bool] = UNSET
    recurring_scheme: Optional[RecurringSchemeOrStr] = UNSET
    duration_period_count: OptionalNullable[int] = UNSET
    duration_interval: OptionalNullable[int] = UNSET
    duration_interval_unit: OptionalNullable[str] = UNSET
    duration_interval_span: OptionalNullable[str] = UNSET
    allow_negative_balance: Optional[bool] = UNSET
    """If set to true, discount is not limited (credits will carry forward to next billing)."""

    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    conversion_limit: OptionalNullable[str] = UNSET
    stackable: Optional[bool] = UNSET
    """A stackable coupon can be combined with other coupons on a Subscription."""

    compounding_strategy: OptionalNullable[CompoundingStrategyOrStr] = UNSET
    """Applicable only to stackable coupons. For ``compound``, Percentage-based discounts will be calculated against the
    remaining price, after prior discounts have been calculated. For ``full-price``, Percentage-based discounts will
    always be calculated against the original item price, before other discounts are applied."""

    use_site_exchange_rate: Optional[bool] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET
    discount_type: Optional[DiscountTypeOrStr] = UNSET
    exclude_mid_period_allocations: Optional[bool] = UNSET
    apply_on_cancel_at_end_of_period: Optional[bool] = UNSET
    apply_on_subscription_expiration: Optional[bool] = UNSET
    coupon_restrictions: Optional[list[CouponRestriction]] = UNSET
    currency_prices: Optional[list[CouponCurrency]] = UNSET
    """Returned in read, find, and list endpoints if the query parameter is provided."""


class CouponDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    code: NotRequired[str]
    description: NotRequired[str]
    amount: NotRequired[float | None]
    amount_in_cents: NotRequired[int | None]
    product_family_id: NotRequired[int]
    product_family_name: NotRequired[str | None]
    start_date: NotRequired[RFC3339DateTime]
    end_date: NotRequired[RFC3339DateTime | None]
    percentage: NotRequired[str | None]
    recurring: NotRequired[bool]
    recurring_scheme: NotRequired[RecurringSchemeOrStr]
    duration_period_count: NotRequired[int | None]
    duration_interval: NotRequired[int | None]
    duration_interval_unit: NotRequired[str | None]
    duration_interval_span: NotRequired[str | None]
    allow_negative_balance: NotRequired[bool]
    archived_at: NotRequired[RFC3339DateTime | None]
    conversion_limit: NotRequired[str | None]
    stackable: NotRequired[bool]
    compounding_strategy: NotRequired[CompoundingStrategyOrStr | None]
    use_site_exchange_rate: NotRequired[bool]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    discount_type: NotRequired[DiscountTypeOrStr]
    exclude_mid_period_allocations: NotRequired[bool]
    apply_on_cancel_at_end_of_period: NotRequired[bool]
    apply_on_subscription_expiration: NotRequired[bool]
    coupon_restrictions: NotRequired[list[CouponRestrictionDict]]
    currency_prices: NotRequired[list[CouponCurrencyDict]]
