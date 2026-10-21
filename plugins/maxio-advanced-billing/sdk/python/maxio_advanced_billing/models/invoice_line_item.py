from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .invoice_line_item_component_cost_data import (
    InvoiceLineItemComponentCostData,
    InvoiceLineItemComponentCostDataDict,
)


class InvoiceLineItem(SdkBaseModel):
    uid: Optional[str] = UNSET
    """Unique identifier for the line item. Useful when cross-referencing the line against individual discounts in the
    ``discounts`` or ``taxes`` lists."""

    title: Optional[str] = UNSET
    """A short descriptor for the charge or item represented by this line."""

    description: Optional[str] = UNSET
    """Detailed description for the charge or item represented by this line. May include proration details in plain
    text.

    Note: this string may contain line breaks that are hints for the best display format on the invoice."""

    quantity: Optional[str] = UNSET
    """The quantity or count of units billed by the line item.

    This is a decimal number represented as a string. (See "About Decimal Numbers".)"""

    unit_price: Optional[str] = UNSET
    """The price per unit for the line item.

    When tiered pricing was used (i.e., not every unit was actually priced at the same price) this will be the blended
    average cost per unit and the ``tiered_unit_price`` field will be set to ``true``."""

    subtotal_amount: Optional[str] = UNSET
    """The line subtotal, generally calculated as ``quantity * unit_price``. This is the canonical amount of record for
    the line - when rounding differences are in play, ``subtotal_amount`` takes precedence over the value derived from
    ``quantity * unit_price`` (which may not have the proper precision to exactly equal this amount)."""

    discount_amount: Optional[str] = UNSET
    """The approximate discount applied to just this line.

    The value is approximated in cases where rounding errors make it difficult to apportion exactly a total discount
    among many lines. Several lines may have been summed prior to applying the discount to arrive at ``discount_amount``
    for the invoice - backing that out to the discount on a single line may introduce rounding or precision errors."""

    tax_amount: Optional[str] = UNSET
    """The approximate tax applied to just this line.

    The value is approximated in cases where rounding errors make it difficult to apportion exactly a total tax among
    many lines. Several lines may have been summed prior to applying the tax rate to arrive at ``tax_amount`` for the
    invoice - backing that out to the tax on a single line may introduce rounding or precision errors."""

    tax_included: Optional[bool] = UNSET
    """Whether the unit price for this line item is tax-inclusive.

    When ``true``, ``unit_price`` already includes tax and ``tax_amount`` represents the portion of the price
    attributable to tax. When ``false``, any applicable tax is added on top of the price.

    The value is inherited from the source price point's ``tax_included`` setting. Custom or ad-hoc line items (which
    have no associated price point) always return ``false``."""

    total_amount: Optional[str] = UNSET
    """The non-canonical total amount for the line.

    ``subtotal_amount`` is the canonical amount for a line. The invoice ``total_amount`` is derived from the sum of the
    line ``subtotal_amount``s and discounts or taxes applied thereafter. Therefore, due to rounding or precision errors,
    the sum of line ``total_amount``s may not equal the invoice ``total_amount``."""

    tiered_unit_price: Optional[bool] = UNSET
    """When ``true``, indicates that the actual pricing scheme for the line was tiered, so the ``unit_price`` shown is
    the blended average for all units."""

    period_range_start: Optional[Date] = UNSET
    """Start date for the period covered by this line. The format is ``"YYYY-MM-DD"``.

    * For periodic charges paid in advance, this date will match the billing date, and the end date will be in the
        future.
    * For periodic charges paid in arrears (e.g., metered charges), this date will be the date of the previous billing,
        and the end date will be the current billing date.
    * For non-periodic charges, this date and the end date will match."""

    period_range_end: Optional[Date] = UNSET
    """End date for the period covered by this line. The format is ``"YYYY-MM-DD"``.

    * For periodic charges paid in advance, this date will match the next (future) billing date.
    * For periodic charges paid in arrears (e.g., metered charges), this date will be the date of the current billing
        date.
    * For non-periodic charges, this date and the start date will match."""

    transaction_id: Optional[int] = UNSET
    product_id: OptionalNullable[int] = UNSET
    """The ID of the product subscribed when the charge was made.

    This may be set even for component charges, so true product-only (non-component) charges will also have a nil
    ``component_id``."""

    product_version: OptionalNullable[int] = UNSET
    """The version of the product subscribed when the charge was made."""

    component_id: OptionalNullable[int] = UNSET
    """The ID of the component being billed. Will be ``nil`` for non-component charges."""

    price_point_id: OptionalNullable[int] = UNSET
    """The price point ID of the component being billed. Will be ``nil`` for non-component charges."""

    billing_schedule_item_id: OptionalNullable[int] = UNSET
    hide: Optional[bool] = UNSET
    component_cost_data: OptionalNullable[InvoiceLineItemComponentCostData] = UNSET
    product_price_point_id: OptionalNullable[int] = UNSET
    """The price point ID of the line item's product"""

    custom_item: Optional[bool] = UNSET
    kind: Optional[str] = UNSET
    prepaid_allocation_expires_at: OptionalNullable[Date] = UNSET
    """The date a prepaid allocation is set to expire. Only present on line items representing prepaid component
    allocations. The format is ``"YYYY-MM-DD"``."""


class InvoiceLineItemDict(TypedDict):
    uid: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    quantity: NotRequired[str]
    unit_price: NotRequired[str]
    subtotal_amount: NotRequired[str]
    discount_amount: NotRequired[str]
    tax_amount: NotRequired[str]
    tax_included: NotRequired[bool]
    total_amount: NotRequired[str]
    tiered_unit_price: NotRequired[bool]
    period_range_start: NotRequired[Date]
    period_range_end: NotRequired[Date]
    transaction_id: NotRequired[int]
    product_id: NotRequired[int | None]
    product_version: NotRequired[int | None]
    component_id: NotRequired[int | None]
    price_point_id: NotRequired[int | None]
    billing_schedule_item_id: NotRequired[int | None]
    hide: NotRequired[bool]
    component_cost_data: NotRequired[InvoiceLineItemComponentCostDataDict | None]
    product_price_point_id: NotRequired[int | None]
    custom_item: NotRequired[bool]
    kind: NotRequired[str]
    prepaid_allocation_expires_at: NotRequired[Date | None]
