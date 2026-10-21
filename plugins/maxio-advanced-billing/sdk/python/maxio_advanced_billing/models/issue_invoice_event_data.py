from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.invoice_consolidation_level import InvoiceConsolidationLevelOrStr
from .enums.invoice_status import InvoiceStatusOrStr


class IssueInvoiceEventData(SdkBaseModel):
    """Example schema for an ``issue_invoice`` event"""

    consolidation_level: InvoiceConsolidationLevelOrStr
    """Consolidation level of the invoice, which is applicable to invoice consolidation. It will hold one of the
    following values:

    * "none": A normal invoice with no consolidation.
    * "child": An invoice segment which has been combined into a consolidated invoice.
    * "parent": A consolidated invoice, whose contents are composed of invoice segments.

    "Parent" invoices do not have lines of their own, but they have subtotals and totals which aggregate the member
    invoice segments.

    See also the `invoice consolidation documentation
    <https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation>`__."""

    from_status: InvoiceStatusOrStr
    """The status of the invoice before event occurrence. See `Invoice Statuses
    <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses>`__
    for more."""

    to_status: InvoiceStatusOrStr
    """The status of the invoice after event occurrence. See `Invoice Statuses
    <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses>`__
    for more."""

    due_amount: str
    """Amount due on the invoice, which is ``total_amount - credit_amount - paid_amount``."""

    total_amount: str
    """The invoice total, which is ``subtotal_amount - discount_amount + tax_amount``.'"""


class IssueInvoiceEventDataDict(TypedDict):
    consolidation_level: InvoiceConsolidationLevelOrStr
    from_status: InvoiceStatusOrStr
    to_status: InvoiceStatusOrStr
    due_amount: str
    total_amount: str
