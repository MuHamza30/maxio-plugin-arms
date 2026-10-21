from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .apply_credit_note_event_data import ApplyCreditNoteEventData, ApplyCreditNoteEventDataDict
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict


class ApplyCreditNoteEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.APPLY_CREDIT_NOTE
    event_data: ApplyCreditNoteEventData
    """Example schema for an ``apply_credit_note`` event"""


class ApplyCreditNoteEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: ApplyCreditNoteEventDataDict
