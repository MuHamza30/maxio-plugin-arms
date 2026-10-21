from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.invoice_consolidation_level import InvoiceConsolidationLevelOrStr
from .unions.invoice_event_payment import InvoiceEventPayment, InvoiceEventPaymentDict


class ApplyPaymentEventData(SdkBaseModel):
    """Example schema for an ``apply_payment`` event"""

    consolidation_level: InvoiceConsolidationLevelOrStr
    memo: str
    """The payment memo"""

    original_amount: str
    """The full, original amount of the payment transaction as a string in full units. Incoming payments can be split
    amongst several invoices, which will result in a ``applied_amount`` less than the ``original_amount``. Example: A
    $100.99 payment, of which $40.11 is applied to this invoice, will have an ``original_amount`` of ``"100.99"``."""

    applied_amount: str
    """The amount of the payment applied to this invoice. Incoming payments can be split amongst several invoices, which
    will result in a ``applied_amount`` less than the ``original_amount``. Example: A $100.99 payment, of which $40.11
    is applied to this invoice, will have an ``applied_amount`` of ``"40.11"``."""

    transaction_time: RFC3339DateTime
    """The time the payment was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
    """

    payment_method: InvoiceEventPayment
    """A nested data structure detailing the method of payment"""

    transaction_id: Optional[int] = UNSET
    """The Chargify id of the original payment"""

    parent_invoice_number: OptionalNullable[int] = UNSET
    remaining_prepayment_amount: OptionalNullable[str] = UNSET
    prepayment: Optional[bool] = UNSET
    external: Optional[bool] = UNSET


class ApplyPaymentEventDataDict(TypedDict):
    consolidation_level: InvoiceConsolidationLevelOrStr
    memo: str
    original_amount: str
    applied_amount: str
    transaction_time: RFC3339DateTime
    payment_method: InvoiceEventPaymentDict
    transaction_id: NotRequired[int]
    parent_invoice_number: NotRequired[int | None]
    remaining_prepayment_amount: NotRequired[str | None]
    prepayment: NotRequired[bool]
    external: NotRequired[bool]
