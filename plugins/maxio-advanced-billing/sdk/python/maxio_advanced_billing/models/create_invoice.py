from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .create_invoice_address import CreateInvoiceAddress, CreateInvoiceAddressDict
from .create_invoice_coupon import CreateInvoiceCoupon, CreateInvoiceCouponDict
from .create_invoice_item import CreateInvoiceItem, CreateInvoiceItemDict
from .enums.create_invoice_status import CreateInvoiceStatus, CreateInvoiceStatusOrStr


class CreateInvoice(SdkBaseModel):
    line_items: Optional[list[CreateInvoiceItem]] = UNSET
    issue_date: Optional[Date] = UNSET
    """Date on which the invoice will be issued (format YYYY-MM-DD). This date is interpreted and validated in your
    site's time zone. It must be today or a date in the past — future dates are not accepted. If omitted, defaults to
    today in your site's time zone."""

    net_terms: Optional[int] = UNSET
    """By default, invoices will be created with a due date matching the date of invoice creation. If a different due
    date is desired, the net_terms parameter can be sent indicating the number of days in advance the due date should
    be."""

    payment_instructions: Optional[str] = UNSET
    memo: Optional[str] = UNSET
    """A custom memo can be sent to override the site's default."""

    seller_address: Optional[CreateInvoiceAddress] = UNSET
    """Overrides the defaults for the site."""

    billing_address: Optional[CreateInvoiceAddress] = UNSET
    """Overrides the default for the customer."""

    shipping_address: Optional[CreateInvoiceAddress] = UNSET
    """Overrides the default for the customer."""

    coupons: Optional[list[CreateInvoiceCoupon]] = UNSET
    status: CreateInvoiceStatusOrStr = CreateInvoiceStatus.OPEN


class CreateInvoiceDict(TypedDict):
    line_items: NotRequired[list[CreateInvoiceItemDict]]
    issue_date: NotRequired[Date]
    net_terms: NotRequired[int]
    payment_instructions: NotRequired[str]
    memo: NotRequired[str]
    seller_address: NotRequired[CreateInvoiceAddressDict]
    billing_address: NotRequired[CreateInvoiceAddressDict]
    shipping_address: NotRequired[CreateInvoiceAddressDict]
    coupons: NotRequired[list[CreateInvoiceCouponDict]]
    status: NotRequired[CreateInvoiceStatusOrStr]
