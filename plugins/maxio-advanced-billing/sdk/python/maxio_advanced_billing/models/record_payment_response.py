from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_pre_payment import InvoicePrePayment, InvoicePrePaymentDict
from .paid_invoice import PaidInvoice, PaidInvoiceDict


class RecordPaymentResponse(SdkBaseModel):
    paid_invoices: Optional[list[PaidInvoice]] = UNSET
    prepayment: OptionalNullable[InvoicePrePayment] = UNSET


class RecordPaymentResponseDict(TypedDict):
    paid_invoices: NotRequired[list[PaidInvoiceDict]]
    prepayment: NotRequired[InvoicePrePaymentDict | None]
