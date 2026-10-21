from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .invoice import Invoice, InvoiceDict


class InvoiceResponse(SdkBaseModel):
    invoice: Invoice


class InvoiceResponseDict(TypedDict):
    invoice: InvoiceDict
