from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.invoice_event_payment_method import InvoiceEventPaymentMethodOrStr


class PaymentMethodExternal(SdkBaseModel):
    details: str | None
    kind: str
    memo: str | None
    type_: InvoiceEventPaymentMethodOrStr = Field(alias="type")


class PaymentMethodExternalDict(TypedDict):
    details: str | None
    kind: str
    memo: str | None
    type_: InvoiceEventPaymentMethodOrStr
