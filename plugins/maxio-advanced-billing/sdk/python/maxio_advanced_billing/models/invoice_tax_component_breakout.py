from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoiceTaxComponentBreakout(SdkBaseModel):
    tax_rule_id: Optional[int] = UNSET
    percentage: Optional[str] = UNSET
    country_code: Optional[str] = UNSET
    subdivision_code: Optional[str] = UNSET
    tax_amount: Optional[str] = UNSET
    taxable_amount: Optional[str] = UNSET
    tax_exempt_amount: Optional[str] = UNSET
    non_taxable_amount: Optional[str] = UNSET
    tax_name: Optional[str] = UNSET
    tax_type: Optional[str] = UNSET
    rate_type: Optional[str] = UNSET
    tax_authority_type: Optional[int] = UNSET
    state_assigned_no: Optional[str] = UNSET
    tax_sub_type: Optional[str] = UNSET


class InvoiceTaxComponentBreakoutDict(TypedDict):
    tax_rule_id: NotRequired[int]
    percentage: NotRequired[str]
    country_code: NotRequired[str]
    subdivision_code: NotRequired[str]
    tax_amount: NotRequired[str]
    taxable_amount: NotRequired[str]
    tax_exempt_amount: NotRequired[str]
    non_taxable_amount: NotRequired[str]
    tax_name: NotRequired[str]
    tax_type: NotRequired[str]
    rate_type: NotRequired[str]
    tax_authority_type: NotRequired[int]
    state_assigned_no: NotRequired[str]
    tax_sub_type: NotRequired[str]
