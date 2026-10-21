from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .renewal_preview_line_item import RenewalPreviewLineItem, RenewalPreviewLineItemDict


class RenewalPreview(SdkBaseModel):
    next_assessment_at: Optional[RFC3339DateTime] = UNSET
    """The timestamp for the subscription’s next renewal"""

    subtotal_in_cents: Optional[int] = UNSET
    """An integer representing the amount of the total pre-tax, pre-discount charges that will be assessed at the next
    renewal"""

    total_tax_in_cents: Optional[int] = UNSET
    """An integer representing the total tax charges that will be assessed at the next renewal"""

    total_discount_in_cents: Optional[int] = UNSET
    """An integer representing the amount of the coupon discounts that will be applied to the next renewal"""

    total_in_cents: Optional[int] = UNSET
    """An integer representing the total amount owed, less any discounts, that will be assessed at the next renewal"""

    existing_balance_in_cents: Optional[int] = UNSET
    """An integer representing the amount of the subscription’s current balance"""

    total_amount_due_in_cents: Optional[int] = UNSET
    """An integer representing the existing_balance_in_cents plus the total_in_cents"""

    uncalculated_taxes: Optional[bool] = UNSET
    """A boolean indicating whether or not additional taxes will be calculated at the time of renewal. This will be true
    if you are using Avalara and the address of the subscription is in one of your defined taxable regions."""

    line_items: Optional[list[RenewalPreviewLineItem]] = UNSET
    """An array of objects representing the individual transactions that will be created at the next renewal"""


class RenewalPreviewDict(TypedDict):
    next_assessment_at: NotRequired[RFC3339DateTime]
    subtotal_in_cents: NotRequired[int]
    total_tax_in_cents: NotRequired[int]
    total_discount_in_cents: NotRequired[int]
    total_in_cents: NotRequired[int]
    existing_balance_in_cents: NotRequired[int]
    total_amount_due_in_cents: NotRequired[int]
    uncalculated_taxes: NotRequired[bool]
    line_items: NotRequired[list[RenewalPreviewLineItemDict]]
