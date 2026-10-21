from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .credit_note import CreditNote, CreditNoteDict
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict


class CreateCreditNoteEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.CREATE_CREDIT_NOTE
    event_data: CreditNote
    """Example schema for an ``create_credit_note`` event"""


class CreateCreditNoteEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: CreditNoteDict
