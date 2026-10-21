from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.invoice_payment_method_type import InvoicePaymentMethodTypeOrStr


class CreatePayment(SdkBaseModel):
    amount: str
    memo: str
    payment_details: str
    payment_method: InvoicePaymentMethodTypeOrStr
    """The type of payment method used. Defaults to other."""


class CreatePaymentDict(TypedDict):
    amount: str
    memo: str
    payment_details: str
    payment_method: InvoicePaymentMethodTypeOrStr
