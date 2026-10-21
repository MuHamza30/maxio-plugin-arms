from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .create_invoice_address import CreateInvoiceAddress, CreateInvoiceAddressDict
from .create_invoice_coupon import CreateInvoiceCoupon, CreateInvoiceCouponDict
from .update_invoice_item import UpdateInvoiceItem, UpdateInvoiceItemDict


class UpdateInvoice(SdkBaseModel):
    """Attributes of a draft ad hoc invoice which can be updated. Only the submitted attributes are changed."""

    line_items: Optional[list[UpdateInvoiceItem]] = UNSET
    """Line item changes to apply. Line items without a ``uid`` are added, line items with a ``uid`` are updated, and
    line items with a ``uid`` and ``_destroy`` set to ``true`` are removed. Existing line items not referenced in the
    array remain unchanged."""

    issue_date: Optional[Date] = UNSET
    """New issue date for the invoice (format YYYY-MM-DD). This date is interpreted and validated in your site's time
    zone. It must be today or a date in the past — future dates are not accepted. The due date is recalculated from the
    issue date and net terms."""

    net_terms: Optional[int] = UNSET
    """Number of days after the issue date on which the invoice is due. The due date is recalculated when net terms or
    the issue date change."""

    payment_instructions: Optional[str] = UNSET
    """Custom payment instructions displayed on the invoice."""

    memo: Optional[str] = UNSET
    """A custom memo displayed on the invoice."""

    seller_address: Optional[CreateInvoiceAddress] = UNSET
    """Replaces the seller address on the invoice"""

    billing_address: Optional[CreateInvoiceAddress] = UNSET
    """Replaces the billing address on the invoice"""

    shipping_address: Optional[CreateInvoiceAddress] = UNSET
    """Replaces the shipping address on the invoice"""

    coupons: Optional[list[CreateInvoiceCoupon]] = UNSET
    """When present, replaces all discounts currently applied to the invoice. Send an empty array to remove all
    discounts."""


class UpdateInvoiceDict(TypedDict):
    line_items: NotRequired[list[UpdateInvoiceItemDict]]
    issue_date: NotRequired[Date]
    net_terms: NotRequired[int]
    payment_instructions: NotRequired[str]
    memo: NotRequired[str]
    seller_address: NotRequired[CreateInvoiceAddressDict]
    billing_address: NotRequired[CreateInvoiceAddressDict]
    shipping_address: NotRequired[CreateInvoiceAddressDict]
    coupons: NotRequired[list[CreateInvoiceCouponDict]]
