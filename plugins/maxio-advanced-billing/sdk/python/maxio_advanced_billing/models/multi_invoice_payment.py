from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .invoice_payment_application import InvoicePaymentApplication, InvoicePaymentApplicationDict


class MultiInvoicePayment(SdkBaseModel):
    transaction_id: Optional[int] = UNSET
    """The numeric ID of the transaction."""

    total_amount: Optional[str] = UNSET
    """Dollar amount of the sum of the paid invoices."""

    currency_code: Optional[str] = UNSET
    """The ISO 4217 currency code (3 character string) representing the currency of invoice transaction."""

    applications: Optional[list[InvoicePaymentApplication]] = UNSET


class MultiInvoicePaymentDict(TypedDict):
    transaction_id: NotRequired[int]
    total_amount: NotRequired[str]
    currency_code: NotRequired[str]
    applications: NotRequired[list[InvoicePaymentApplicationDict]]
