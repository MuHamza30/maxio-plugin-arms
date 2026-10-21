from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .invoice_payer_change import InvoicePayerChange, InvoicePayerChangeDict


class CustomerPayerChange(SdkBaseModel):
    before: InvoicePayerChange
    after: InvoicePayerChange


class CustomerPayerChangeDict(TypedDict):
    before: InvoicePayerChangeDict
    after: InvoicePayerChangeDict
