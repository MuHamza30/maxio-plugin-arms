from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict
from .void_invoice_event_data import VoidInvoiceEventData, VoidInvoiceEventDataDict


class VoidInvoiceEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.VOID_INVOICE
    event_data: VoidInvoiceEventData
    """Example schema for an ``void_invoice`` event"""


class VoidInvoiceEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: VoidInvoiceEventDataDict
