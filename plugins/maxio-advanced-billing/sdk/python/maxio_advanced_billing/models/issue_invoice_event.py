from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict
from .issue_invoice_event_data import IssueInvoiceEventData, IssueInvoiceEventDataDict


class IssueInvoiceEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.ISSUE_INVOICE
    event_data: IssueInvoiceEventData
    """Example schema for an ``issue_invoice`` event"""


class IssueInvoiceEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: IssueInvoiceEventDataDict
