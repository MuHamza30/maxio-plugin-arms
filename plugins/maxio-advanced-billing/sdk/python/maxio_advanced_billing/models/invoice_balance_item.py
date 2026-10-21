from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoiceBalanceItem(SdkBaseModel):
    uid: Optional[str] = UNSET
    number: Optional[str] = UNSET
    outstanding_amount: Optional[str] = UNSET


class InvoiceBalanceItemDict(TypedDict):
    uid: NotRequired[str]
    number: NotRequired[str]
    outstanding_amount: NotRequired[str]
