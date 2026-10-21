from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.allocation_preview_direction import AllocationPreviewDirectionOrStr
from .enums.allocation_preview_line_item_kind import AllocationPreviewLineItemKindOrStr
from .enums.line_item_transaction_type import LineItemTransactionTypeOrStr


class AllocationPreviewLineItem(SdkBaseModel):
    transaction_type: Optional[LineItemTransactionTypeOrStr] = UNSET
    """A handle for the line item transaction type"""

    kind: Optional[AllocationPreviewLineItemKindOrStr] = UNSET
    """A handle for the line item kind for allocation preview"""

    amount_in_cents: Optional[int] = UNSET
    memo: Optional[str] = UNSET
    discount_amount_in_cents: Optional[int] = UNSET
    taxable_amount_in_cents: Optional[int] = UNSET
    component_id: Optional[int] = UNSET
    component_handle: Optional[str] = UNSET
    direction: Optional[AllocationPreviewDirectionOrStr] = UNSET
    """Visible when using Fine-grained Component Control."""


class AllocationPreviewLineItemDict(TypedDict):
    transaction_type: NotRequired[LineItemTransactionTypeOrStr]
    kind: NotRequired[AllocationPreviewLineItemKindOrStr]
    amount_in_cents: NotRequired[int]
    memo: NotRequired[str]
    discount_amount_in_cents: NotRequired[int]
    taxable_amount_in_cents: NotRequired[int]
    component_id: NotRequired[int]
    component_handle: NotRequired[str]
    direction: NotRequired[AllocationPreviewDirectionOrStr]
