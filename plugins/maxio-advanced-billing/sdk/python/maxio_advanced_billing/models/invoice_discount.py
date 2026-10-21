from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.invoice_discount_source_type import InvoiceDiscountSourceTypeOrStr
from .enums.invoice_discount_type import InvoiceDiscountTypeOrStr
from .invoice_discount_breakout import InvoiceDiscountBreakout, InvoiceDiscountBreakoutDict


class InvoiceDiscount(SdkBaseModel):
    uid: Optional[str] = UNSET
    title: Optional[str] = UNSET
    description: OptionalNullable[str] = UNSET
    code: Optional[str] = UNSET
    source_type: Optional[InvoiceDiscountSourceTypeOrStr] = UNSET
    source_id: Optional[int] = UNSET
    discount_type: Optional[InvoiceDiscountTypeOrStr] = UNSET
    percentage: Optional[str] = UNSET
    eligible_amount: Optional[str] = UNSET
    discount_amount: Optional[str] = UNSET
    transaction_id: Optional[int] = UNSET
    line_item_breakouts: Optional[list[InvoiceDiscountBreakout]] = UNSET


class InvoiceDiscountDict(TypedDict):
    uid: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str | None]
    code: NotRequired[str]
    source_type: NotRequired[InvoiceDiscountSourceTypeOrStr]
    source_id: NotRequired[int]
    discount_type: NotRequired[InvoiceDiscountTypeOrStr]
    percentage: NotRequired[str]
    eligible_amount: NotRequired[str]
    discount_amount: NotRequired[str]
    transaction_id: NotRequired[int]
    line_item_breakouts: NotRequired[list[InvoiceDiscountBreakoutDict]]
