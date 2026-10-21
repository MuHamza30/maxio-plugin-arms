from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_line_item_pricing_detail import InvoiceLineItemPricingDetail, InvoiceLineItemPricingDetailDict


class InvoiceLineItemEventData(SdkBaseModel):
    uid: Optional[str] = UNSET
    title: Optional[str] = UNSET
    description: Optional[str] = UNSET
    quantity: Optional[int] = UNSET
    quantity_delta: OptionalNullable[int] = UNSET
    unit_price: Optional[str] = UNSET
    period_range_start: Optional[str] = UNSET
    period_range_end: Optional[str] = UNSET
    amount: Optional[str] = UNSET
    line_references: Optional[str] = UNSET
    pricing_details_index: OptionalNullable[int] = UNSET
    pricing_details: Optional[list[InvoiceLineItemPricingDetail]] = UNSET
    tax_code: OptionalNullable[str] = UNSET
    tax_amount: Optional[str] = UNSET
    product_id: Optional[int] = UNSET
    product_price_point_id: OptionalNullable[int] = UNSET
    price_point_id: OptionalNullable[int] = UNSET
    component_id: OptionalNullable[int] = UNSET
    billing_schedule_item_id: OptionalNullable[int] = UNSET
    custom_item: OptionalNullable[bool] = UNSET


class InvoiceLineItemEventDataDict(TypedDict):
    uid: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    quantity: NotRequired[int]
    quantity_delta: NotRequired[int | None]
    unit_price: NotRequired[str]
    period_range_start: NotRequired[str]
    period_range_end: NotRequired[str]
    amount: NotRequired[str]
    line_references: NotRequired[str]
    pricing_details_index: NotRequired[int | None]
    pricing_details: NotRequired[list[InvoiceLineItemPricingDetailDict]]
    tax_code: NotRequired[str | None]
    tax_amount: NotRequired[str]
    product_id: NotRequired[int]
    product_price_point_id: NotRequired[int | None]
    price_point_id: NotRequired[int | None]
    component_id: NotRequired[int | None]
    billing_schedule_item_id: NotRequired[int | None]
    custom_item: NotRequired[bool | None]
