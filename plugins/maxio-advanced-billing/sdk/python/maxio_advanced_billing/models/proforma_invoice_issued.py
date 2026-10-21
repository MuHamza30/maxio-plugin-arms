from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, RFC3339DateTime, SdkBaseModel
from .invoice_line_item_event_data import InvoiceLineItemEventData, InvoiceLineItemEventDataDict


class ProformaInvoiceIssued(SdkBaseModel):
    uid: str
    number: str
    role: str
    delivery_date: Date
    created_at: RFC3339DateTime
    due_amount: str
    paid_amount: str
    tax_amount: str
    total_amount: str
    product_name: str
    line_items: list[InvoiceLineItemEventData]


class ProformaInvoiceIssuedDict(TypedDict):
    uid: str
    number: str
    role: str
    delivery_date: Date
    created_at: RFC3339DateTime
    due_amount: str
    paid_amount: str
    tax_amount: str
    total_amount: str
    product_name: str
    line_items: list[InvoiceLineItemEventDataDict]
