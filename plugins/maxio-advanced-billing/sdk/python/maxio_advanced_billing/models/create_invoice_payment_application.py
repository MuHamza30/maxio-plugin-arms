from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateInvoicePaymentApplication(SdkBaseModel):
    invoice_uid: str
    """Unique identifier for the invoice. It has the prefix "inv_" followed by alphanumeric characters."""

    amount: str
    """Dollar amount of the invoice payment (eg. "10.50" => $10.50)."""


class CreateInvoicePaymentApplicationDict(TypedDict):
    invoice_uid: str
    amount: str
