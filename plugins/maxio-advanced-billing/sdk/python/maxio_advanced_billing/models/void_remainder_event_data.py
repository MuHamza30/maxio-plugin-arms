from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .credit_note import CreditNote, CreditNoteDict


class VoidRemainderEventData(SdkBaseModel):
    """Example schema for an ``void_remainder`` event"""

    credit_note_attributes: CreditNote
    memo: str
    """The memo provided during invoice remainder voiding."""

    applied_amount: str
    """The amount of the void."""

    transaction_time: RFC3339DateTime
    """The time the refund was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
    """


class VoidRemainderEventDataDict(TypedDict):
    credit_note_attributes: CreditNoteDict
    memo: str
    applied_amount: str
    transaction_time: RFC3339DateTime
