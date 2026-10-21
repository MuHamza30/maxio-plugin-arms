from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .apply_debit_note_event_data import ApplyDebitNoteEventData, ApplyDebitNoteEventDataDict
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict


class ApplyDebitNoteEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.APPLY_DEBIT_NOTE
    event_data: ApplyDebitNoteEventData
    """Example schema for an ``apply_debit_note`` event"""


class ApplyDebitNoteEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: ApplyDebitNoteEventDataDict
