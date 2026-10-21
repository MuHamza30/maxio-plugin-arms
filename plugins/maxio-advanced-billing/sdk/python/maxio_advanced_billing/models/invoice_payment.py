from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .invoice_payment_method import InvoicePaymentMethod, InvoicePaymentMethodDict


class InvoicePayment(SdkBaseModel):
    transaction_time: Optional[RFC3339DateTime] = UNSET
    memo: Optional[str] = UNSET
    original_amount: Optional[str] = UNSET
    applied_amount: Optional[str] = UNSET
    payment_method: Optional[InvoicePaymentMethod] = UNSET
    transaction_id: Optional[int] = UNSET
    prepayment: Optional[bool] = UNSET
    gateway_handle: OptionalNullable[str] = UNSET
    gateway_used: Optional[str] = UNSET
    gateway_transaction_id: OptionalNullable[str] = UNSET
    """The transaction ID for the payment as returned from the payment gateway"""

    received_on: OptionalNullable[Date] = UNSET
    """Date reflecting when the payment was received from a customer. Must be in the past. Applicable only to
    ``external`` payments."""

    uid: Optional[str] = UNSET


class InvoicePaymentDict(TypedDict):
    transaction_time: NotRequired[RFC3339DateTime]
    memo: NotRequired[str]
    original_amount: NotRequired[str]
    applied_amount: NotRequired[str]
    payment_method: NotRequired[InvoicePaymentMethodDict]
    transaction_id: NotRequired[int]
    prepayment: NotRequired[bool]
    gateway_handle: NotRequired[str | None]
    gateway_used: NotRequired[str]
    gateway_transaction_id: NotRequired[str | None]
    received_on: NotRequired[Date | None]
    uid: NotRequired[str]
