from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_invoice_payment import CreateInvoicePayment, CreateInvoicePaymentDict
from .enums.invoice_payment_type import InvoicePaymentTypeOrStr


class CreateInvoicePaymentRequest(SdkBaseModel):
    payment: CreateInvoicePayment
    type_: Optional[InvoicePaymentTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of payment to be applied to an Invoice. Defaults to external."""


class CreateInvoicePaymentRequestDict(TypedDict):
    payment: CreateInvoicePaymentDict
    type_: NotRequired[InvoicePaymentTypeOrStr]
