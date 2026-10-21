from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.proforma_invoice_tax_source_type import ProformaInvoiceTaxSourceTypeOrStr
from .invoice_tax_breakout import InvoiceTaxBreakout, InvoiceTaxBreakoutDict


class ProformaInvoiceTax(SdkBaseModel):
    uid: Optional[str] = UNSET
    title: Optional[str] = UNSET
    source_type: Optional[ProformaInvoiceTaxSourceTypeOrStr] = UNSET
    percentage: Optional[str] = UNSET
    taxable_amount: Optional[str] = UNSET
    tax_amount: Optional[str] = UNSET
    line_item_breakouts: Optional[list[InvoiceTaxBreakout]] = UNSET


class ProformaInvoiceTaxDict(TypedDict):
    uid: NotRequired[str]
    title: NotRequired[str]
    source_type: NotRequired[ProformaInvoiceTaxSourceTypeOrStr]
    percentage: NotRequired[str]
    taxable_amount: NotRequired[str]
    tax_amount: NotRequired[str]
    line_item_breakouts: NotRequired[list[InvoiceTaxBreakoutDict]]
