from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_invoice import CreateInvoice, CreateInvoiceDict


class CreateInvoiceRequest(SdkBaseModel):
    invoice: CreateInvoice


class CreateInvoiceRequestDict(TypedDict):
    invoice: CreateInvoiceDict
