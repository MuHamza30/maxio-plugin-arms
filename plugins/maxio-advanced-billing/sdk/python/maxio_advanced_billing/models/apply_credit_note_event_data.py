from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .applied_credit_note_data import AppliedCreditNoteData, AppliedCreditNoteDataDict


class ApplyCreditNoteEventData(SdkBaseModel):
    """Example schema for an ``apply_credit_note`` event"""

    uid: str
    """Unique identifier for the credit note application. It is generated automatically by Chargify and has the prefix
    "cdt_" followed by alphanumeric characters."""

    credit_note_number: str
    """A unique, identifying string that appears on the credit note and in places it is referenced."""

    credit_note_uid: str
    """Unique identifier for the credit note. It is generated automatically by Chargify and has the prefix "cn_"
    followed by alphanumeric characters."""

    original_amount: str
    """The full, original amount of the credit note."""

    applied_amount: str
    """The amount of the credit note applied to invoice."""

    transaction_time: Optional[RFC3339DateTime] = UNSET
    """The time the credit note was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
    """

    memo: OptionalNullable[str] = UNSET
    """The credit note memo."""

    role: Optional[str] = UNSET
    """The role of the credit note (e.g. 'general')"""

    consolidated_invoice: Optional[bool] = UNSET
    """Shows whether it was applied to consolidated invoice or not."""

    applied_credit_notes: Optional[list[AppliedCreditNoteData]] = UNSET
    """List of credit notes applied to children invoices (if consolidated invoice)"""


class ApplyCreditNoteEventDataDict(TypedDict):
    uid: str
    credit_note_number: str
    credit_note_uid: str
    original_amount: str
    applied_amount: str
    transaction_time: NotRequired[RFC3339DateTime]
    memo: NotRequired[str | None]
    role: NotRequired[str]
    consolidated_invoice: NotRequired[bool]
    applied_credit_notes: NotRequired[list[AppliedCreditNoteDataDict]]
