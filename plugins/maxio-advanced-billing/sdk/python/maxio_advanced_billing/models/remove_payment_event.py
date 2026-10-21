from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict
from .remove_payment_event_data import RemovePaymentEventData, RemovePaymentEventDataDict


class RemovePaymentEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.REMOVE_PAYMENT
    event_data: RemovePaymentEventData
    """Example schema for an ``remove_payment`` event"""


class RemovePaymentEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: RemovePaymentEventDataDict
