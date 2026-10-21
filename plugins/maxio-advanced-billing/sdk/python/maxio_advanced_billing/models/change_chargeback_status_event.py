from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .change_chargeback_status_event_data import ChangeChargebackStatusEventData, ChangeChargebackStatusEventDataDict
from .enums.invoice_event_type import InvoiceEventType, InvoiceEventTypeOrStr
from .invoice import Invoice, InvoiceDict


class ChangeChargebackStatusEvent(SdkBaseModel):
    id: int
    timestamp: RFC3339DateTime
    invoice: Invoice
    event_type: InvoiceEventTypeOrStr = InvoiceEventType.CHANGE_CHARGEBACK_STATUS
    event_data: ChangeChargebackStatusEventData
    """Example schema for an ``change_chargeback_status`` event"""


class ChangeChargebackStatusEventDict(TypedDict):
    id: int
    timestamp: RFC3339DateTime
    invoice: InvoiceDict
    event_type: InvoiceEventTypeOrStr
    event_data: ChangeChargebackStatusEventDataDict
