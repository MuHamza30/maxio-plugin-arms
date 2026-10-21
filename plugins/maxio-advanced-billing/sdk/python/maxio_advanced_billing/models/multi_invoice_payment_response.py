from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .multi_invoice_payment import MultiInvoicePayment, MultiInvoicePaymentDict


class MultiInvoicePaymentResponse(SdkBaseModel):
    payment: MultiInvoicePayment


class MultiInvoicePaymentResponseDict(TypedDict):
    payment: MultiInvoicePaymentDict
