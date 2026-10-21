from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.invoice_discount_type import InvoiceDiscountTypeOrStr
from .enums.proforma_invoice_discount_source_type import ProformaInvoiceDiscountSourceTypeOrStr
from .invoice_discount_breakout import InvoiceDiscountBreakout, InvoiceDiscountBreakoutDict


class ProformaInvoiceDiscount(SdkBaseModel):
    uid: Optional[str] = UNSET
    title: Optional[str] = UNSET
    code: Optional[str] = UNSET
    source_type: Optional[ProformaInvoiceDiscountSourceTypeOrStr] = UNSET
    discount_type: Optional[InvoiceDiscountTypeOrStr] = UNSET
    eligible_amount: Optional[str] = UNSET
    discount_amount: Optional[str] = UNSET
    line_item_breakouts: Optional[list[InvoiceDiscountBreakout]] = UNSET


class ProformaInvoiceDiscountDict(TypedDict):
    uid: NotRequired[str]
    title: NotRequired[str]
    code: NotRequired[str]
    source_type: NotRequired[ProformaInvoiceDiscountSourceTypeOrStr]
    discount_type: NotRequired[InvoiceDiscountTypeOrStr]
    eligible_amount: NotRequired[str]
    discount_amount: NotRequired[str]
    line_item_breakouts: NotRequired[list[InvoiceDiscountBreakoutDict]]
