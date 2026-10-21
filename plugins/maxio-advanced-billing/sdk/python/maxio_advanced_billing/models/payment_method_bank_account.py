from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.invoice_event_payment_method import InvoiceEventPaymentMethodOrStr


class PaymentMethodBankAccount(SdkBaseModel):
    masked_account_number: str
    masked_routing_number: str
    type_: InvoiceEventPaymentMethodOrStr = Field(alias="type")


class PaymentMethodBankAccountDict(TypedDict):
    masked_account_number: str
    masked_routing_number: str
    type_: InvoiceEventPaymentMethodOrStr
