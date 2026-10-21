from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .failed_payment_event_data import FailedPaymentEventData, FailedPaymentEventDataDict
from .invoice import Invoice, InvoiceDict


class FailedPaymentEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.FAILED_PAYMENT
    event_data: FailedPaymentEventData
    """Example schema for an ``failed_payment`` event"""


class FailedPaymentEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: FailedPaymentEventDataDict
