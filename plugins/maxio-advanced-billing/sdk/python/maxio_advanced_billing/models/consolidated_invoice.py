from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .invoice import Invoice, InvoiceDict


class ConsolidatedInvoice(SdkBaseModel):
    invoices: Optional[list[Invoice]] = UNSET


class ConsolidatedInvoiceDict(TypedDict):
    invoices: NotRequired[list[InvoiceDict]]
