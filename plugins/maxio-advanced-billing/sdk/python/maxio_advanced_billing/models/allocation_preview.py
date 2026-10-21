from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .allocation_preview_item import AllocationPreviewItem, AllocationPreviewItemDict
from .allocation_preview_line_item import AllocationPreviewLineItem, AllocationPreviewLineItemDict
from .enums.allocation_preview_direction import AllocationPreviewDirectionOrStr


class AllocationPreview(SdkBaseModel):
    start_date: Optional[RFC3339DateTime] = UNSET
    end_date: Optional[RFC3339DateTime] = UNSET
    subtotal_in_cents: Optional[int] = UNSET
    total_tax_in_cents: Optional[int] = UNSET
    total_discount_in_cents: Optional[int] = UNSET
    total_in_cents: Optional[int] = UNSET
    direction: Optional[AllocationPreviewDirectionOrStr] = UNSET
    proration_scheme: Optional[str] = UNSET
    line_items: Optional[list[AllocationPreviewLineItem]] = UNSET
    accrue_charge: Optional[bool] = UNSET
    allocations: Optional[list[AllocationPreviewItem]] = UNSET
    period_type: Optional[str] = UNSET
    existing_balance_in_cents: Optional[int] = UNSET
    """An integer representing the amount of the subscription's current balance"""


class AllocationPreviewDict(TypedDict):
    start_date: NotRequired[RFC3339DateTime]
    end_date: NotRequired[RFC3339DateTime]
    subtotal_in_cents: NotRequired[int]
    total_tax_in_cents: NotRequired[int]
    total_discount_in_cents: NotRequired[int]
    total_in_cents: NotRequired[int]
    direction: NotRequired[AllocationPreviewDirectionOrStr]
    proration_scheme: NotRequired[str]
    line_items: NotRequired[list[AllocationPreviewLineItemDict]]
    accrue_charge: NotRequired[bool]
    allocations: NotRequired[list[AllocationPreviewItemDict]]
    period_type: NotRequired[str]
    existing_balance_in_cents: NotRequired[int]
