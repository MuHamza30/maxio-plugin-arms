from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.invoice_status import InvoiceStatusOrStr


class PaidInvoice(SdkBaseModel):
    invoice_id: Optional[str] = UNSET
    """The uid of the paid invoice"""

    status: Optional[InvoiceStatusOrStr] = UNSET
    """The current status of the invoice. See `Invoice Statuses
    <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses>`__
    for more."""

    due_amount: Optional[str] = UNSET
    """The remaining due amount on the invoice"""

    paid_amount: Optional[str] = UNSET
    """The total amount paid on this invoice (including any prior payments)"""


class PaidInvoiceDict(TypedDict):
    invoice_id: NotRequired[str]
    status: NotRequired[InvoiceStatusOrStr]
    due_amount: NotRequired[str]
    paid_amount: NotRequired[str]
