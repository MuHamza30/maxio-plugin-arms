from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.proforma_invoice_tax_source_type import ProformaInvoiceTaxSourceTypeOrStr
from .invoice_tax_breakout import InvoiceTaxBreakout, InvoiceTaxBreakoutDict
from .invoice_tax_component_breakout import InvoiceTaxComponentBreakout, InvoiceTaxComponentBreakoutDict


class InvoiceTax(SdkBaseModel):
    uid: Optional[str] = UNSET
    title: Optional[str] = UNSET
    description: OptionalNullable[str] = UNSET
    source_type: Optional[ProformaInvoiceTaxSourceTypeOrStr] = UNSET
    source_id: Optional[int] = UNSET
    percentage: Optional[str] = UNSET
    taxable_amount: Optional[str] = UNSET
    tax_amount: Optional[str] = UNSET
    transaction_id: Optional[int] = UNSET
    line_item_breakouts: Optional[list[InvoiceTaxBreakout]] = UNSET
    tax_component_breakouts: Optional[list[InvoiceTaxComponentBreakout]] = UNSET
    eu_vat: Optional[bool] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    tax_exempt_amount: Optional[str] = UNSET


class InvoiceTaxDict(TypedDict):
    uid: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str | None]
    source_type: NotRequired[ProformaInvoiceTaxSourceTypeOrStr]
    source_id: NotRequired[int]
    percentage: NotRequired[str]
    taxable_amount: NotRequired[str]
    tax_amount: NotRequired[str]
    transaction_id: NotRequired[int]
    line_item_breakouts: NotRequired[list[InvoiceTaxBreakoutDict]]
    tax_component_breakouts: NotRequired[list[InvoiceTaxComponentBreakoutDict]]
    eu_vat: NotRequired[bool]
    type_: NotRequired[str]
    tax_exempt_amount: NotRequired[str]
