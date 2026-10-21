from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .apply_payment_event_data import ApplyPaymentEventData, ApplyPaymentEventDataDict
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict


class ApplyPaymentEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.APPLY_PAYMENT
    event_data: ApplyPaymentEventData
    """Example schema for an ``apply_payment`` event"""


class ApplyPaymentEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: ApplyPaymentEventDataDict
