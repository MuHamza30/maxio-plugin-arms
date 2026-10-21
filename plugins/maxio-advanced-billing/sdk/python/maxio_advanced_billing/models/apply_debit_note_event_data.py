from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ApplyDebitNoteEventData(SdkBaseModel):
    """Example schema for an ``apply_debit_note`` event"""

    debit_note_number: str
    """A unique, identifying string that appears on the debit note and in places it is referenced."""

    debit_note_uid: str
    """Unique identifier for the debit note. It is generated automatically by Chargify and has the prefix "db_" followed
    by alphanumeric characters."""

    original_amount: str
    """The full, original amount of the debit note."""

    applied_amount: str
    """The amount of the debit note applied to invoice."""

    memo: OptionalNullable[str] = UNSET
    """The debit note memo."""

    transaction_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The time the debit note was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
    """


class ApplyDebitNoteEventDataDict(TypedDict):
    debit_note_number: str
    debit_note_uid: str
    original_amount: str
    applied_amount: str
    memo: NotRequired[str | None]
    transaction_time: NotRequired[RFC3339DateTime | None]
