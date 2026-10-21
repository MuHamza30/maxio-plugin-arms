from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .credit_note import CreditNote, CreditNoteDict


class VoidInvoiceEventData(SdkBaseModel):
    """Example schema for an ``void_invoice`` event"""

    credit_note_attributes: CreditNote | None
    memo: str | None
    """The memo provided during invoice voiding."""

    applied_amount: str | None
    """The amount of the void."""

    transaction_time: RFC3339DateTime | None
    """The time the refund was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
    """

    is_advance_invoice: bool
    """If true, the invoice is an advance invoice."""

    reason: str
    """The reason for the void."""


class VoidInvoiceEventDataDict(TypedDict):
    credit_note_attributes: CreditNoteDict | None
    memo: str | None
    applied_amount: str | None
    transaction_time: RFC3339DateTime | None
    is_advance_invoice: bool
    reason: str
