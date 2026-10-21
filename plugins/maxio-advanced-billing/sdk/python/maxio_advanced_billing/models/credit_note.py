from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .credit_note_application import CreditNoteApplication, CreditNoteApplicationDict
from .credit_note_line_item import CreditNoteLineItem, CreditNoteLineItemDict
from .enums.credit_note_status import CreditNoteStatusOrStr
from .invoice_address import InvoiceAddress, InvoiceAddressDict
from .invoice_customer import InvoiceCustomer, InvoiceCustomerDict
from .invoice_discount import InvoiceDiscount, InvoiceDiscountDict
from .invoice_refund import InvoiceRefund, InvoiceRefundDict
from .invoice_seller import InvoiceSeller, InvoiceSellerDict
from .invoice_tax import InvoiceTax, InvoiceTaxDict
from .origin_invoice import OriginInvoice, OriginInvoiceDict


class CreditNote(SdkBaseModel):
    uid: Optional[str] = UNSET
    """Unique identifier for the credit note. It is generated automatically by Chargify and has the prefix "cn_"
    followed by alphanumeric characters."""

    site_id: Optional[int] = UNSET
    """ID of the site to which the credit note belongs."""

    customer_id: Optional[int] = UNSET
    """ID of the customer to which the credit note belongs."""

    subscription_id: Optional[int] = UNSET
    """ID of the subscription that generated the credit note."""

    number: Optional[str] = UNSET
    """A unique, identifying string that appears on the credit note and in places it is referenced.

    While the UID is long and not appropriate to show to customers, the number is usually shorter and consumable by the
    customer and the merchant alike."""

    sequence_number: Optional[int] = UNSET
    """A monotonically increasing number assigned to credit notes as they are created. This number is unique within a
    site and can be used to sort and order credit notes."""

    issue_date: Optional[Date] = UNSET
    """Date the credit note was issued to the customer. This is the date that the credit was made available for
    application, and may come before it is fully applied.

    The format is ``"YYYY-MM-DD"``."""

    applied_date: Optional[Date] = UNSET
    """Credit notes are applied to invoices to offset invoiced amounts - they reduce the amount due. This field is the
    date the credit note became fully applied to invoices.

    If the credit note has been partially applied, this field will not have a value until it has been fully applied.

    The format is ``"YYYY-MM-DD"``."""

    status: Optional[CreditNoteStatusOrStr] = UNSET
    """Current status of the credit note."""

    currency: Optional[str] = UNSET
    """The ISO 4217 currency code (3 character string) representing the currency of the credit note amount fields."""

    memo: Optional[str] = UNSET
    """The memo printed on credit note, which is a description of the reason for the credit."""

    seller: Optional[InvoiceSeller] = UNSET
    """Information about the seller (merchant) listed on the masthead of the credit note."""

    customer: Optional[InvoiceCustomer] = UNSET
    """Information about the customer who is owner or recipient of the credited subscription."""

    billing_address: Optional[InvoiceAddress] = UNSET
    """The billing address of the credit subscription."""

    shipping_address: Optional[InvoiceAddress] = UNSET
    """The shipping address of the credited subscription."""

    subtotal_amount: Optional[str] = UNSET
    """Subtotal of the credit note, which is the sum of all line items before discounts or taxes. Note that this is a
    positive amount representing the credit back to the customer."""

    discount_amount: Optional[str] = UNSET
    """Total discount applied to the credit note. Note that this is a positive amount representing the discount amount
    being credited back to the customer (i.e., a credit on an earlier discount). For example, if the original purchase
    was $1.00 and the original discount was $0.10, a credit of $0.50 of the original purchase (half) would have a
    discount credit of $0.05 (also half)."""

    tax_amount: Optional[str] = UNSET
    """Total tax of the credit note. Note that this is a positive amount representing a previously taxed amount being
    credited back to the customer (i.e., a credit of an earlier tax). For example, if the original purchase was $1.00
    and the original tax was $0.10, a credit of $0.50 of the original purchase (half) would also have a tax credit of
    $0.05 (also half)."""

    total_amount: Optional[str] = UNSET
    """The credit note total, which is ``subtotal_amount - discount_amount + tax_amount``."""

    applied_amount: Optional[str] = UNSET
    """The amount of the credit note that has already been applied to invoices."""

    remaining_amount: Optional[str] = UNSET
    """The amount of the credit note remaining to be applied to invoices, which is ``total_amount - applied_amount``."""

    line_items: Optional[list[CreditNoteLineItem]] = UNSET
    """Line items on the credit note."""

    discounts: Optional[list[InvoiceDiscount]] = UNSET
    taxes: Optional[list[InvoiceTax]] = UNSET
    applications: Optional[list[CreditNoteApplication]] = UNSET
    refunds: Optional[list[InvoiceRefund]] = UNSET
    origin_invoices: Optional[list[OriginInvoice]] = UNSET
    """An array of origin invoices for the credit note. Learn more about `Origin Invoice from our docs
    <https://maxio.zendesk.com/hc/en-us/articles/24252261284749-Credit-Notes-Proration#origin-invoices>`__."""


class CreditNoteDict(TypedDict):
    uid: NotRequired[str]
    site_id: NotRequired[int]
    customer_id: NotRequired[int]
    subscription_id: NotRequired[int]
    number: NotRequired[str]
    sequence_number: NotRequired[int]
    issue_date: NotRequired[Date]
    applied_date: NotRequired[Date]
    status: NotRequired[CreditNoteStatusOrStr]
    currency: NotRequired[str]
    memo: NotRequired[str]
    seller: NotRequired[InvoiceSellerDict]
    customer: NotRequired[InvoiceCustomerDict]
    billing_address: NotRequired[InvoiceAddressDict]
    shipping_address: NotRequired[InvoiceAddressDict]
    subtotal_amount: NotRequired[str]
    discount_amount: NotRequired[str]
    tax_amount: NotRequired[str]
    total_amount: NotRequired[str]
    applied_amount: NotRequired[str]
    remaining_amount: NotRequired[str]
    line_items: NotRequired[list[CreditNoteLineItemDict]]
    discounts: NotRequired[list[InvoiceDiscountDict]]
    taxes: NotRequired[list[InvoiceTaxDict]]
    applications: NotRequired[list[CreditNoteApplicationDict]]
    refunds: NotRequired[list[InvoiceRefundDict]]
    origin_invoices: NotRequired[list[OriginInvoiceDict]]
