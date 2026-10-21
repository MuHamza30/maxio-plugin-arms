from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .invoice import Invoice, InvoiceDict


class ListInvoicesResponse(SdkBaseModel):
    invoices: list[Invoice]


class ListInvoicesResponseDict(TypedDict):
    invoices: list[InvoiceDict]
