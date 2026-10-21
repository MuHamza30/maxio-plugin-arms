from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProformaInvoicePayment(SdkBaseModel):
    memo: Optional[str] = UNSET
    original_amount: Optional[str] = UNSET
    applied_amount: Optional[str] = UNSET
    prepayment: Optional[bool] = UNSET


class ProformaInvoicePaymentDict(TypedDict):
    memo: NotRequired[str]
    original_amount: NotRequired[str]
    applied_amount: NotRequired[str]
    prepayment: NotRequired[bool]
