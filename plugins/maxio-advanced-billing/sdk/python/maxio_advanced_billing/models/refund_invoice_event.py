from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict
from .refund_invoice_event_data import RefundInvoiceEventData, RefundInvoiceEventDataDict


class RefundInvoiceEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.REFUND_INVOICE
    event_data: RefundInvoiceEventData
    """Example schema for an ``refund_invoice`` event"""


class RefundInvoiceEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: RefundInvoiceEventDataDict
