from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.line_item_kind import LineItemKindOrStr
from .enums.line_item_transaction_type import LineItemTransactionTypeOrStr


class RenewalPreviewLineItem(SdkBaseModel):
    transaction_type: Optional[LineItemTransactionTypeOrStr] = UNSET
    """A handle for the line item transaction type"""

    kind: Optional[LineItemKindOrStr] = UNSET
    """A handle for the line item kind"""

    amount_in_cents: Optional[int] = UNSET
    memo: Optional[str] = UNSET
    discount_amount_in_cents: Optional[int] = UNSET
    taxable_amount_in_cents: Optional[int] = UNSET
    product_id: Optional[int] = UNSET
    product_name: Optional[str] = UNSET
    component_id: Optional[int] = UNSET
    component_handle: Optional[str] = UNSET
    component_name: Optional[str] = UNSET
    product_handle: Optional[str] = UNSET
    period_range_start: Optional[str] = UNSET
    period_range_end: Optional[str] = UNSET


class RenewalPreviewLineItemDict(TypedDict):
    transaction_type: NotRequired[LineItemTransactionTypeOrStr]
    kind: NotRequired[LineItemKindOrStr]
    amount_in_cents: NotRequired[int]
    memo: NotRequired[str]
    discount_amount_in_cents: NotRequired[int]
    taxable_amount_in_cents: NotRequired[int]
    product_id: NotRequired[int]
    product_name: NotRequired[str]
    component_id: NotRequired[int]
    component_handle: NotRequired[str]
    component_name: NotRequired[str]
    product_handle: NotRequired[str]
    period_range_start: NotRequired[str]
    period_range_end: NotRequired[str]
