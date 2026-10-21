from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.invoice_payment_method_type import InvoicePaymentMethodTypeOrStr


class FailedPaymentEventData(SdkBaseModel):
    """Example schema for an ``failed_payment`` event"""

    amount_in_cents: int
    """The monetary value of the payment, expressed in cents."""

    applied_amount: int
    """The monetary value of the payment, expressed in dollars."""

    memo: OptionalNullable[str] = UNSET
    """The memo passed when the payment was created."""

    payment_method: InvoicePaymentMethodTypeOrStr
    transaction_id: int
    """The transaction ID of the failed payment."""


class FailedPaymentEventDataDict(TypedDict):
    amount_in_cents: int
    applied_amount: int
    memo: NotRequired[str | None]
    payment_method: InvoicePaymentMethodTypeOrStr
    transaction_id: int
