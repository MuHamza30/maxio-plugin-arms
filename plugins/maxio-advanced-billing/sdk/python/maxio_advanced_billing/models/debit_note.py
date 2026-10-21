from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .credit_note_line_item import CreditNoteLineItem, CreditNoteLineItemDict
from .enums.debit_note_role import DebitNoteRoleOrStr
from .enums.debit_note_status import DebitNoteStatusOrStr
from .invoice_address import InvoiceAddress, InvoiceAddressDict
from .invoice_customer import InvoiceCustomer, InvoiceCustomerDict
from .invoice_discount import InvoiceDiscount, InvoiceDiscountDict
from .invoice_refund import InvoiceRefund, InvoiceRefundDict
from .invoice_seller import InvoiceSeller, InvoiceSellerDict
from .invoice_tax import InvoiceTax, InvoiceTaxDict


class DebitNote(SdkBaseModel):
    uid: Optional[str] = UNSET
    """Unique identifier for the debit note. It is generated automatically by Chargify and has the prefix "db_" followed
    by alphanumeric characters."""

    site_id: Optional[int] = UNSET
    """ID of the site to which the debit note belongs."""

    customer_id: Optional[int] = UNSET
    """ID of the customer to which the debit note belongs."""

    subscription_id: Optional[int] = UNSET
    """ID of the subscription that generated the debit note."""

    number: Optional[int] = UNSET
    """A unique identifier that appears on the debit note and in places it is referenced."""

    sequence_number: Optional[int] = UNSET
    """A monotonically increasing number assigned to debit notes as they are created."""

    origin_credit_note_uid: Optional[str] = UNSET
    """Unique identifier for the connected credit note. It is generated automatically by Chargify and has the prefix
    "cn_" followed by alphanumeric characters.

    While the UID is long and not appropriate to show to customers, the number is usually shorter and consumable by the
    customer and the merchant alike."""

    origin_credit_note_number: Optional[str] = UNSET
    """A unique identifying string of the connected credit note."""

    issue_date: Optional[Date] = UNSET
    """Date the document was issued to the customer. This is the date that the document was made available for payment.

    The format is "YYYY-MM-DD"."""

    applied_date: Optional[Date] = UNSET
    """Debit notes are applied to invoices to offset invoiced amounts - they adjust the amount due. This field is the
    date the debit note document became fully applied to the invoice.

    The format is "YYYY-MM-DD"."""

    due_date: Optional[Date] = UNSET
    """Date the document is due for payment. The format is "YYYY-MM-DD"."""

    status: Optional[DebitNoteStatusOrStr] = UNSET
    """Current status of the debit note."""

    memo: Optional[str] = UNSET
    """The memo printed on debit note, which is a description of the reason for the debit."""

    role: Optional[DebitNoteRoleOrStr] = UNSET
    """The role of the debit note."""

    currency: Optional[str] = UNSET
    """The ISO 4217 currency code (3 character string) representing the currency of the credit note amount fields."""

    seller: Optional[InvoiceSeller] = UNSET
    """Information about the seller (merchant) listed on the masthead of the debit note."""

    customer: Optional[InvoiceCustomer] = UNSET
    """Information about the customer who is the owner or recipient of the debited subscription."""

    billing_address: Optional[InvoiceAddress] = UNSET
    """The billing address of the debited subscription."""

    shipping_address: Optional[InvoiceAddress] = UNSET
    """The shipping address of the debited subscription."""

    line_items: Optional[list[CreditNoteLineItem]] = UNSET
    """Line items on the debit note."""

    discounts: Optional[list[InvoiceDiscount]] = UNSET
    taxes: Optional[list[InvoiceTax]] = UNSET
    refunds: Optional[list[InvoiceRefund]] = UNSET


class DebitNoteDict(TypedDict):
    uid: NotRequired[str]
    site_id: NotRequired[int]
    customer_id: NotRequired[int]
    subscription_id: NotRequired[int]
    number: NotRequired[int]
    sequence_number: NotRequired[int]
    origin_credit_note_uid: NotRequired[str]
    origin_credit_note_number: NotRequired[str]
    issue_date: NotRequired[Date]
    applied_date: NotRequired[Date]
    due_date: NotRequired[Date]
    status: NotRequired[DebitNoteStatusOrStr]
    memo: NotRequired[str]
    role: NotRequired[DebitNoteRoleOrStr]
    currency: NotRequired[str]
    seller: NotRequired[InvoiceSellerDict]
    customer: NotRequired[InvoiceCustomerDict]
    billing_address: NotRequired[InvoiceAddressDict]
    shipping_address: NotRequired[InvoiceAddressDict]
    line_items: NotRequired[list[CreditNoteLineItemDict]]
    discounts: NotRequired[list[InvoiceDiscountDict]]
    taxes: NotRequired[list[InvoiceTaxDict]]
    refunds: NotRequired[list[InvoiceRefundDict]]
