from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoiceTaxBreakout(SdkBaseModel):
    uid: Optional[str] = UNSET
    taxable_amount: Optional[str] = UNSET
    tax_amount: Optional[str] = UNSET
    tax_exempt_amount: Optional[str] = UNSET


class InvoiceTaxBreakoutDict(TypedDict):
    uid: NotRequired[str]
    taxable_amount: NotRequired[str]
    tax_amount: NotRequired[str]
    tax_exempt_amount: NotRequired[str]
