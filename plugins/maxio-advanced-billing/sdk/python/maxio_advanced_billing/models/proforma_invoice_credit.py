from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProformaInvoiceCredit(SdkBaseModel):
    uid: Optional[str] = UNSET
    memo: Optional[str] = UNSET
    original_amount: Optional[str] = UNSET
    applied_amount: Optional[str] = UNSET


class ProformaInvoiceCreditDict(TypedDict):
    uid: NotRequired[str]
    memo: NotRequired[str]
    original_amount: NotRequired[str]
    applied_amount: NotRequired[str]
