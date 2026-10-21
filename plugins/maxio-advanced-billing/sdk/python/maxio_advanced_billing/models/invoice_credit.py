from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class InvoiceCredit(SdkBaseModel):
    uid: Optional[str] = UNSET
    credit_note_number: Optional[str] = UNSET
    credit_note_uid: Optional[str] = UNSET
    transaction_time: Optional[RFC3339DateTime] = UNSET
    memo: Optional[str] = UNSET
    original_amount: Optional[str] = UNSET
    applied_amount: Optional[str] = UNSET


class InvoiceCreditDict(TypedDict):
    uid: NotRequired[str]
    credit_note_number: NotRequired[str]
    credit_note_uid: NotRequired[str]
    transaction_time: NotRequired[RFC3339DateTime]
    memo: NotRequired[str]
    original_amount: NotRequired[str]
    applied_amount: NotRequired[str]
