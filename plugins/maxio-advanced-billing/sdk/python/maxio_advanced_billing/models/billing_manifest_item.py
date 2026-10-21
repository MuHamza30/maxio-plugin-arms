from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.billing_manifest_line_item_kind import BillingManifestLineItemKindOrStr
from .enums.line_item_transaction_type import LineItemTransactionTypeOrStr


class BillingManifestItem(SdkBaseModel):
    transaction_type: Optional[LineItemTransactionTypeOrStr] = UNSET
    """A handle for the line item transaction type"""

    kind: Optional[BillingManifestLineItemKindOrStr] = UNSET
    """A handle for the billing manifest line item kind"""

    amount_in_cents: Optional[int] = UNSET
    memo: Optional[str] = UNSET
    discount_amount_in_cents: Optional[int] = UNSET
    taxable_amount_in_cents: Optional[int] = UNSET
    component_id: Optional[int] = UNSET
    component_handle: Optional[str] = UNSET
    component_name: Optional[str] = UNSET
    product_id: Optional[int] = UNSET
    product_handle: Optional[str] = UNSET
    product_name: Optional[str] = UNSET
    period_range_start: Optional[str] = UNSET
    period_range_end: Optional[str] = UNSET


class BillingManifestItemDict(TypedDict):
    transaction_type: NotRequired[LineItemTransactionTypeOrStr]
    kind: NotRequired[BillingManifestLineItemKindOrStr]
    amount_in_cents: NotRequired[int]
    memo: NotRequired[str]
    discount_amount_in_cents: NotRequired[int]
    taxable_amount_in_cents: NotRequired[int]
    component_id: NotRequired[int]
    component_handle: NotRequired[str]
    component_name: NotRequired[str]
    product_id: NotRequired[int]
    product_handle: NotRequired[str]
    product_name: NotRequired[str]
    period_range_start: NotRequired[str]
    period_range_end: NotRequired[str]
