from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .unions.invoice_event_payment import InvoiceEventPayment, InvoiceEventPaymentDict


class RemovePaymentEventData(SdkBaseModel):
    """Example schema for an ``remove_payment`` event"""

    transaction_id: int
    """Transaction ID of the original payment that was removed"""

    memo: str
    """Memo of the original payment"""

    original_amount: Optional[str] = UNSET
    """Full amount of the original payment"""

    applied_amount: str
    """Applied amount of the original payment"""

    transaction_time: RFC3339DateTime
    """Transaction time of the original payment, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
    """

    payment_method: InvoiceEventPayment
    """A nested data structure detailing the method of payment"""

    prepayment: bool
    """The flag that shows whether the original payment was a prepayment or not"""


class RemovePaymentEventDataDict(TypedDict):
    transaction_id: int
    memo: str
    original_amount: NotRequired[str]
    applied_amount: str
    transaction_time: RFC3339DateTime
    payment_method: InvoiceEventPaymentDict
    prepayment: bool
