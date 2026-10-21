from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.invoice_event_payment_method import InvoiceEventPaymentMethodOrStr


class PaymentMethodApplePay(SdkBaseModel):
    type_: InvoiceEventPaymentMethodOrStr = Field(alias="type")


class PaymentMethodApplePayDict(TypedDict):
    type_: InvoiceEventPaymentMethodOrStr
