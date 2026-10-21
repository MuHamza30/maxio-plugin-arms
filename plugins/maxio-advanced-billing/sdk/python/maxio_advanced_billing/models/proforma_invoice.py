from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .available_actions import AvailableActions, AvailableActionsDict
from .enums.collection_method import CollectionMethodOrStr
from .enums.invoice_consolidation_level import InvoiceConsolidationLevelOrStr
from .enums.proforma_invoice_role import ProformaInvoiceRoleOrStr
from .enums.proforma_invoice_status import ProformaInvoiceStatusOrStr
from .invoice_address import InvoiceAddress, InvoiceAddressDict
from .invoice_custom_field import InvoiceCustomField, InvoiceCustomFieldDict
from .invoice_customer import InvoiceCustomer, InvoiceCustomerDict
from .invoice_line_item import InvoiceLineItem, InvoiceLineItemDict
from .invoice_seller import InvoiceSeller, InvoiceSellerDict
from .proforma_invoice_credit import ProformaInvoiceCredit, ProformaInvoiceCreditDict
from .proforma_invoice_discount import ProformaInvoiceDiscount, ProformaInvoiceDiscountDict
from .proforma_invoice_payment import ProformaInvoicePayment, ProformaInvoicePaymentDict
from .proforma_invoice_tax import ProformaInvoiceTax, ProformaInvoiceTaxDict


class ProformaInvoice(SdkBaseModel):
    uid: Optional[str] = UNSET
    site_id: Optional[int] = UNSET
    customer_id: OptionalNullable[int] = UNSET
    subscription_id: OptionalNullable[int] = UNSET
    number: OptionalNullable[int] = UNSET
    sequence_number: OptionalNullable[int] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    delivery_date: Optional[Date] = UNSET
    status: Optional[ProformaInvoiceStatusOrStr] = UNSET
    collection_method: Optional[CollectionMethodOrStr] = UNSET
    """The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options
    are - ``invoice``, ``automatic``. For current Relationship Invoicing Architecture valid options are -
    ``remittance``, ``automatic``, ``prepaid``."""

    payment_instructions: Optional[str] = UNSET
    currency: Optional[str] = UNSET
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

    product_name: Optional[str] = UNSET
    product_family_name: Optional[str] = UNSET
    role: Optional[ProformaInvoiceRoleOrStr] = UNSET
    """'proforma' value is deprecated in favor of proforma_adhoc and proforma_automatic."""

    seller: Optional[InvoiceSeller] = UNSET
    """Information about the seller (merchant) listed on the masthead of the invoice."""

    customer: Optional[InvoiceCustomer] = UNSET
    """Information about the customer who is owner or recipient of the invoiced subscription."""

    memo: Optional[str] = UNSET
    billing_address: Optional[InvoiceAddress] = UNSET
    shipping_address: Optional[InvoiceAddress] = UNSET
    subtotal_amount: Optional[str] = UNSET
    discount_amount: Optional[str] = UNSET
    tax_amount: Optional[str] = UNSET
    total_amount: Optional[str] = UNSET
    credit_amount: Optional[str] = UNSET
    paid_amount: Optional[str] = UNSET
    refund_amount: Optional[str] = UNSET
    due_amount: Optional[str] = UNSET
    line_items: Optional[list[InvoiceLineItem]] = UNSET
    discounts: Optional[list[ProformaInvoiceDiscount]] = UNSET
    taxes: Optional[list[ProformaInvoiceTax]] = UNSET
    credits: Optional[list[ProformaInvoiceCredit]] = UNSET
    payments: Optional[list[ProformaInvoicePayment]] = UNSET
    custom_fields: Optional[list[InvoiceCustomField]] = UNSET
    public_url: OptionalNullable[str] = UNSET
    available_actions: Optional[AvailableActions] = UNSET


class ProformaInvoiceDict(TypedDict):
    uid: NotRequired[str]
    site_id: NotRequired[int]
    customer_id: NotRequired[int | None]
    subscription_id: NotRequired[int | None]
    number: NotRequired[int | None]
    sequence_number: NotRequired[int | None]
    created_at: NotRequired[RFC3339DateTime]
    delivery_date: NotRequired[Date]
    status: NotRequired[ProformaInvoiceStatusOrStr]
    collection_method: NotRequired[CollectionMethodOrStr]
    payment_instructions: NotRequired[str]
    currency: NotRequired[str]
    consolidation_level: NotRequired[InvoiceConsolidationLevelOrStr]
    product_name: NotRequired[str]
    product_family_name: NotRequired[str]
    role: NotRequired[ProformaInvoiceRoleOrStr]
    seller: NotRequired[InvoiceSellerDict]
    customer: NotRequired[InvoiceCustomerDict]
    memo: NotRequired[str]
    billing_address: NotRequired[InvoiceAddressDict]
    shipping_address: NotRequired[InvoiceAddressDict]
    subtotal_amount: NotRequired[str]
    discount_amount: NotRequired[str]
    tax_amount: NotRequired[str]
    total_amount: NotRequired[str]
    credit_amount: NotRequired[str]
    paid_amount: NotRequired[str]
    refund_amount: NotRequired[str]
    due_amount: NotRequired[str]
    line_items: NotRequired[list[InvoiceLineItemDict]]
    discounts: NotRequired[list[ProformaInvoiceDiscountDict]]
    taxes: NotRequired[list[ProformaInvoiceTaxDict]]
    credits: NotRequired[list[ProformaInvoiceCreditDict]]
    payments: NotRequired[list[ProformaInvoicePaymentDict]]
    custom_fields: NotRequired[list[InvoiceCustomFieldDict]]
    public_url: NotRequired[str | None]
    available_actions: NotRequired[AvailableActionsDict]
