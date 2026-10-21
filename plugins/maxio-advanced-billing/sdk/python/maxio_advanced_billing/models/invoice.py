from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.collection_method import CollectionMethodOrStr
from .enums.invoice_consolidation_level import InvoiceConsolidationLevelOrStr
from .enums.invoice_role import InvoiceRoleOrStr
from .enums.invoice_status import InvoiceStatusOrStr
from .invoice_address import InvoiceAddress, InvoiceAddressDict
from .invoice_avatax_details import InvoiceAvataxDetails, InvoiceAvataxDetailsDict
from .invoice_credit import InvoiceCredit, InvoiceCreditDict
from .invoice_custom_field import InvoiceCustomField, InvoiceCustomFieldDict
from .invoice_customer import InvoiceCustomer, InvoiceCustomerDict
from .invoice_debit import InvoiceDebit, InvoiceDebitDict
from .invoice_discount import InvoiceDiscount, InvoiceDiscountDict
from .invoice_display_settings import InvoiceDisplaySettings, InvoiceDisplaySettingsDict
from .invoice_line_item import InvoiceLineItem, InvoiceLineItemDict
from .invoice_payer import InvoicePayer, InvoicePayerDict
from .invoice_payment import InvoicePayment, InvoicePaymentDict
from .invoice_previous_balance import InvoicePreviousBalance, InvoicePreviousBalanceDict
from .invoice_refund import InvoiceRefund, InvoiceRefundDict
from .invoice_seller import InvoiceSeller, InvoiceSellerDict
from .invoice_tax import InvoiceTax, InvoiceTaxDict


class Invoice(SdkBaseModel):
    id: Optional[int] = UNSET
    uid: Optional[str] = UNSET
    """Unique identifier for the invoice. It is generated automatically by Chargify and has the prefix "inv_" followed
    by alphanumeric characters."""

    site_id: Optional[int] = UNSET
    """ID of the site to which the invoice belongs."""

    customer_id: Optional[int] = UNSET
    """ID of the customer to which the invoice belongs."""

    subscription_id: Optional[int] = UNSET
    """ID of the subscription that generated the invoice."""

    number: Optional[str] = UNSET
    """A unique, identifying string that appears on the invoice and in places the invoice is referenced.

    While the UID is long and not appropriate to show to customers, the number is usually shorter and consumable by the
    customer and the merchant alike."""

    sequence_number: Optional[int] = UNSET
    """A monotonically increasing number assigned to invoices as they are created. This number is unique within a site
    and can be used to sort and order invoices."""

    transaction_time: Optional[RFC3339DateTime] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET
    issue_date: Optional[Date] = UNSET
    """Date the invoice was issued to the customer. This is the date that the invoice was made available for payment.

    The format is ``"YYYY-MM-DD"``."""

    due_date: Optional[Date] = UNSET
    """Date the invoice is due.

    The format is ``"YYYY-MM-DD"``."""

    paid_date: OptionalNullable[Date] = UNSET
    """Date the invoice became fully paid.

    If partial payments are applied to the invoice, this date will not be present until payment has been made in full.

    The format is ``"YYYY-MM-DD"``."""

    status: Optional[InvoiceStatusOrStr] = UNSET
    """The current status of the invoice. See `Invoice Statuses
    <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses>`__
    for more."""

    role: Optional[InvoiceRoleOrStr] = UNSET
    parent_invoice_id: OptionalNullable[int] = UNSET
    collection_method: Optional[CollectionMethodOrStr] = UNSET
    """The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options
    are - ``invoice``, ``automatic``. For current Relationship Invoicing Architecture valid options are -
    ``remittance``, ``automatic``, ``prepaid``."""

    payment_instructions: Optional[str] = UNSET
    """A message that is printed on the invoice when it is marked for remittance collection. It is intended to describe
    to the customer how they may make payment, and is configured by the merchant."""

    currency: Optional[str] = UNSET
    """The ISO 4217 currency code (3 character string) representing the currency of invoice transaction."""

    consolidation_level: Optional[InvoiceConsolidationLevelOrStr] = UNSET
    """Consolidation level of the invoice, which is applicable to invoice consolidation. It will hold one of the
    following values:

    * "none": A normal invoice with no consolidation.
    * "child": An invoice segment which has been combined into a consolidated invoice.
    * "parent": A consolidated invoice, whose contents are composed of invoice segments.

    "Parent" invoices do not have lines of their own, but they have subtotals and totals which aggregate the member
    invoice segments.

    See also the `invoice consolidation documentation
    <https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation>`__."""

    parent_invoice_uid: OptionalNullable[str] = UNSET
    """For invoices with ``consolidation_level`` of ``child``, this specifies the UID of the parent (consolidated)
    invoice."""

    subscription_group_id: OptionalNullable[int] = UNSET
    parent_invoice_number: OptionalNullable[int] = UNSET
    """For invoices with ``consolidation_level`` of ``child``, this specifies the number of the parent (consolidated)
    invoice."""

    group_primary_subscription_id: OptionalNullable[int] = UNSET
    """For invoices with ``consolidation_level`` of ``parent``, this specifies the ID of the subscription which was the
    primary subscription of the subscription group that generated the invoice."""

    product_name: Optional[str] = UNSET
    """The name of the product subscribed when the invoice was generated."""

    product_family_name: Optional[str] = UNSET
    """The name of the product family subscribed when the invoice was generated."""

    seller: Optional[InvoiceSeller] = UNSET
    """Information about the seller (merchant) listed on the masthead of the invoice."""

    customer: Optional[InvoiceCustomer] = UNSET
    """Information about the customer who is owner or recipient of the invoiced subscription."""

    payer: Optional[InvoicePayer] = UNSET
    recipient_emails: Optional[list[str]] = UNSET
    net_terms: Optional[int] = UNSET
    memo: Optional[str] = UNSET
    """The memo printed on invoices of any collection type. This message is in control of the merchant."""

    billing_address: Optional[InvoiceAddress] = UNSET
    """The invoice billing address."""

    shipping_address: Optional[InvoiceAddress] = UNSET
    """The invoice shipping address."""

    subtotal_amount: Optional[str] = UNSET
    """Subtotal of the invoice, which is the sum of all line items before discounts or taxes."""

    discount_amount: Optional[str] = UNSET
    """Total discount applied to the invoice."""

    tax_amount: Optional[str] = UNSET
    """Total tax on the invoice."""

    total_amount: Optional[str] = UNSET
    """The invoice total, which is ``subtotal_amount - discount_amount + tax_amount``."""

    credit_amount: Optional[str] = UNSET
    """The amount of credit (from credit notes) applied to this invoice.

    Credits offset the amount due from the customer."""

    debit_amount: Optional[str] = UNSET
    refund_amount: Optional[str] = UNSET
    paid_amount: Optional[str] = UNSET
    """The amount paid on the invoice by the customer."""

    due_amount: Optional[str] = UNSET
    """Amount due on the invoice, which is ``total_amount - credit_amount - paid_amount``."""

    line_items: Optional[list[InvoiceLineItem]] = UNSET
    """Line items on the invoice."""

    discounts: Optional[list[InvoiceDiscount]] = UNSET
    taxes: Optional[list[InvoiceTax]] = UNSET
    credits: Optional[list[InvoiceCredit]] = UNSET
    debits: Optional[list[InvoiceDebit]] = UNSET
    refunds: Optional[list[InvoiceRefund]] = UNSET
    payments: Optional[list[InvoicePayment]] = UNSET
    custom_fields: Optional[list[InvoiceCustomField]] = UNSET
    display_settings: Optional[InvoiceDisplaySettings] = UNSET
    avatax_details: Optional[InvoiceAvataxDetails] = UNSET
    public_url: Optional[str] = UNSET
    """The public URL of the invoice"""

    previous_balance_data: Optional[InvoicePreviousBalance] = UNSET
    public_url_expires_on: Optional[Date] = UNSET
    """The format is ``"YYYY-MM-DD"``."""

    branding_theme_id: OptionalNullable[int] = UNSET
    """The ID of the Branding Theme associated with this invoice. This value represents the Branding Theme used for
    invoice theming, such as themed invoice rendering. Available only when Branding Themes are enabled for the site."""


class InvoiceDict(TypedDict):
    id: NotRequired[int]
    uid: NotRequired[str]
    site_id: NotRequired[int]
    customer_id: NotRequired[int]
    subscription_id: NotRequired[int]
    number: NotRequired[str]
    sequence_number: NotRequired[int]
    transaction_time: NotRequired[RFC3339DateTime]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    issue_date: NotRequired[Date]
    due_date: NotRequired[Date]
    paid_date: NotRequired[Date | None]
    status: NotRequired[InvoiceStatusOrStr]
    role: NotRequired[InvoiceRoleOrStr]
    parent_invoice_id: NotRequired[int | None]
    collection_method: NotRequired[CollectionMethodOrStr]
    payment_instructions: NotRequired[str]
    currency: NotRequired[str]
    consolidation_level: NotRequired[InvoiceConsolidationLevelOrStr]
    parent_invoice_uid: NotRequired[str | None]
    subscription_group_id: NotRequired[int | None]
    parent_invoice_number: NotRequired[int | None]
    group_primary_subscription_id: NotRequired[int | None]
    product_name: NotRequired[str]
    product_family_name: NotRequired[str]
    seller: NotRequired[InvoiceSellerDict]
    customer: NotRequired[InvoiceCustomerDict]
    payer: NotRequired[InvoicePayerDict]
    recipient_emails: NotRequired[list[str]]
    net_terms: NotRequired[int]
    memo: NotRequired[str]
    billing_address: NotRequired[InvoiceAddressDict]
    shipping_address: NotRequired[InvoiceAddressDict]
    subtotal_amount: NotRequired[str]
    discount_amount: NotRequired[str]
    tax_amount: NotRequired[str]
    total_amount: NotRequired[str]
    credit_amount: NotRequired[str]
    debit_amount: NotRequired[str]
    refund_amount: NotRequired[str]
    paid_amount: NotRequired[str]
    due_amount: NotRequired[str]
    line_items: NotRequired[list[InvoiceLineItemDict]]
    discounts: NotRequired[list[InvoiceDiscountDict]]
    taxes: NotRequired[list[InvoiceTaxDict]]
    credits: NotRequired[list[InvoiceCreditDict]]
    debits: NotRequired[list[InvoiceDebitDict]]
    refunds: NotRequired[list[InvoiceRefundDict]]
    payments: NotRequired[list[InvoicePaymentDict]]
    custom_fields: NotRequired[list[InvoiceCustomFieldDict]]
    display_settings: NotRequired[InvoiceDisplaySettingsDict]
    avatax_details: NotRequired[InvoiceAvataxDetailsDict]
    public_url: NotRequired[str]
    previous_balance_data: NotRequired[InvoicePreviousBalanceDict]
    public_url_expires_on: NotRequired[Date]
    branding_theme_id: NotRequired[int | None]
