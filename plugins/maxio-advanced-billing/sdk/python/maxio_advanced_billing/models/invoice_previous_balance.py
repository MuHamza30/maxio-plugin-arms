from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .invoice_balance_item import InvoiceBalanceItem, InvoiceBalanceItemDict


class InvoicePreviousBalance(SdkBaseModel):
    captured_at: Optional[RFC3339DateTime] = UNSET
    invoices: Optional[list[InvoiceBalanceItem]] = UNSET


class InvoicePreviousBalanceDict(TypedDict):
    captured_at: NotRequired[RFC3339DateTime]
    invoices: NotRequired[list[InvoiceBalanceItemDict]]
