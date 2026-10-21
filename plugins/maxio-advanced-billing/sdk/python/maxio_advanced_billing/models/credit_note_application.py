from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class CreditNoteApplication(SdkBaseModel):
    uid: Optional[str] = UNSET
    transaction_time: Optional[RFC3339DateTime] = UNSET
    invoice_uid: Optional[str] = UNSET
    memo: Optional[str] = UNSET
    applied_amount: Optional[str] = UNSET


class CreditNoteApplicationDict(TypedDict):
    uid: NotRequired[str]
    transaction_time: NotRequired[RFC3339DateTime]
    invoice_uid: NotRequired[str]
    memo: NotRequired[str]
    applied_amount: NotRequired[str]
