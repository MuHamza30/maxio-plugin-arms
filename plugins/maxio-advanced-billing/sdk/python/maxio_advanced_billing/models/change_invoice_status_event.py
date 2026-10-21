from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .change_invoice_status_event_data import ChangeInvoiceStatusEventData, ChangeInvoiceStatusEventDataDict
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict


class ChangeInvoiceStatusEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.CHANGE_INVOICE_STATUS
    event_data: ChangeInvoiceStatusEventData
    """Example schema for an ``change_invoice_status`` event"""


class ChangeInvoiceStatusEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: ChangeInvoiceStatusEventDataDict
