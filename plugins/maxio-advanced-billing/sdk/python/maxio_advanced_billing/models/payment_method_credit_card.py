from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.invoice_event_payment_method import InvoiceEventPaymentMethodOrStr


class PaymentMethodCreditCard(SdkBaseModel):
    card_brand: str
    card_expiration: Optional[str] = UNSET
    last_four: OptionalNullable[str] = UNSET
    masked_card_number: str
    type_: InvoiceEventPaymentMethodOrStr = Field(alias="type")


class PaymentMethodCreditCardDict(TypedDict):
    card_brand: str
    card_expiration: NotRequired[str]
    last_four: NotRequired[str | None]
    masked_card_number: str
    type_: InvoiceEventPaymentMethodOrStr
