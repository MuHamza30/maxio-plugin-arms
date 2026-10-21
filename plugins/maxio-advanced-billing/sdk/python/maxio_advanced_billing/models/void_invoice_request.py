from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .void_invoice import VoidInvoice, VoidInvoiceDict


class VoidInvoiceRequest(SdkBaseModel):
    void: VoidInvoice


class VoidInvoiceRequestDict(TypedDict):
    void: VoidInvoiceDict
