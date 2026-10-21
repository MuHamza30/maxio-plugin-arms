from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.compounding_strategy import CompoundingStrategyOrStr
from .unions.percentage import Percentage, PercentageDict


class CouponPayload(SdkBaseModel):
    name: Optional[str] = UNSET
    """Required when creating a new coupon. This name is not displayed to customers and is limited to 255 characters."""

    code: Optional[str] = UNSET
    """Required when creating a new coupon. The code is limited to 255 characters. May contain uppercase alphanumeric
    characters and these special characters (which allow for email addresses to be used): “%”, “@”, “+”, “-”, “_”, and
    “.”."""

    description: Optional[str] = UNSET
    """Required when creating a new coupon. A description of the coupon that can be displayed to customers in
    transactions and on statements. The description is limited to 255 characters."""

    percentage: Optional[Percentage] = UNSET
    """Required when creating a new percentage coupon. Can't be used together with amount_in_cents. Percentage
    discount."""

    amount_in_cents: Optional[int] = UNSET
    """Required when creating a new flat amount coupon. Can't be used together with percentage. Flat USD discount."""

    allow_negative_balance: Optional[bool] = UNSET
    """If set to true, discount is not limited (credits will carry forward to next billing). Can't be used together with
    restrictions."""

    recurring: Optional[bool] = UNSET
    end_date: Optional[Date] = UNSET
    """After the end of the given day, this coupon code will be invalid for new signups. Recurring discounts started
    before this date will continue to recur even after this date."""

    product_family_id: Optional[str] = UNSET
    stackable: Optional[bool] = UNSET
    """A stackable coupon can be combined with other coupons on a Subscription."""

    compounding_strategy: Optional[CompoundingStrategyOrStr] = UNSET
    """Applicable only to stackable coupons. For ``compound``, Percentage-based discounts will be calculated against the
    remaining price, after prior discounts have been calculated. For ``full-price``, Percentage-based discounts will
    always be calculated against the original item price, before other discounts are applied."""

    exclude_mid_period_allocations: Optional[bool] = UNSET
    apply_on_cancel_at_end_of_period: Optional[bool] = UNSET
    apply_on_subscription_expiration: Optional[bool] = UNSET


class CouponPayloadDict(TypedDict):
    name: NotRequired[str]
    code: NotRequired[str]
    description: NotRequired[str]
    percentage: NotRequired[PercentageDict]
    amount_in_cents: NotRequired[int]
    allow_negative_balance: NotRequired[bool]
    recurring: NotRequired[bool]
    end_date: NotRequired[Date]
    product_family_id: NotRequired[str]
    stackable: NotRequired[bool]
    compounding_strategy: NotRequired[CompoundingStrategyOrStr]
    exclude_mid_period_allocations: NotRequired[bool]
    apply_on_cancel_at_end_of_period: NotRequired[bool]
    apply_on_subscription_expiration: NotRequired[bool]
