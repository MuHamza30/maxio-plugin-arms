from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoiceDiscountBreakout(SdkBaseModel):
    uid: Optional[str] = UNSET
    eligible_amount: Optional[str] = UNSET
    discount_amount: Optional[str] = UNSET


class InvoiceDiscountBreakoutDict(TypedDict):
    uid: NotRequired[str]
    eligible_amount: NotRequired[str]
    discount_amount: NotRequired[str]
