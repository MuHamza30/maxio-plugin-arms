from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.invoice_event_payment_method import InvoiceEventPaymentMethodOrStr


class PaymentMethodPaypal(SdkBaseModel):
    email: EmailStr
    type_: InvoiceEventPaymentMethodOrStr = Field(alias="type")


class PaymentMethodPaypalDict(TypedDict):
    email: EmailStr
    type_: InvoiceEventPaymentMethodOrStr
