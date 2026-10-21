from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .invoice_line_item_event_data import InvoiceLineItemEventData, InvoiceLineItemEventDataDict


class InvoiceIssued(SdkBaseModel):
    uid: str
    number: str
    role: str
    due_date: Date | None
    issue_date: str
    """Invoice issue date. Can be an empty string if value is missing."""

    paid_date: str
    """Paid date. Can be an empty string if value is missing."""

    due_amount: str
    paid_amount: str
    tax_amount: str
    refund_amount: str
    total_amount: str
    status_amount: str
    product_name: str
    consolidation_level: str
    line_items: list[InvoiceLineItemEventData]


class InvoiceIssuedDict(TypedDict):
    uid: str
    number: str
    role: str
    due_date: Date | None
    issue_date: str
    paid_date: str
    due_amount: str
    paid_amount: str
    tax_amount: str
    refund_amount: str
    total_amount: str
    status_amount: str
    product_name: str
    consolidation_level: str
    line_items: list[InvoiceLineItemEventDataDict]
