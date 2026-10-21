from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_multi_invoice_payment import CreateMultiInvoicePayment, CreateMultiInvoicePaymentDict


class CreateMultiInvoicePaymentRequest(SdkBaseModel):
    payment: CreateMultiInvoicePayment


class CreateMultiInvoicePaymentRequestDict(TypedDict):
    payment: CreateMultiInvoicePaymentDict
