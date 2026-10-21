from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.debit_note_role import DebitNoteRoleOrStr


class InvoiceDebit(SdkBaseModel):
    uid: Optional[str] = UNSET
    debit_note_number: Optional[str] = UNSET
    debit_note_uid: Optional[str] = UNSET
    role: Optional[DebitNoteRoleOrStr] = UNSET
    """The role of the debit note."""

    transaction_time: Optional[RFC3339DateTime] = UNSET
    memo: Optional[str] = UNSET
    original_amount: Optional[str] = UNSET
    applied_amount: Optional[str] = UNSET


class InvoiceDebitDict(TypedDict):
    uid: NotRequired[str]
    debit_note_number: NotRequired[str]
    debit_note_uid: NotRequired[str]
    role: NotRequired[DebitNoteRoleOrStr]
    transaction_time: NotRequired[RFC3339DateTime]
    memo: NotRequired[str]
    original_amount: NotRequired[str]
    applied_amount: NotRequired[str]
