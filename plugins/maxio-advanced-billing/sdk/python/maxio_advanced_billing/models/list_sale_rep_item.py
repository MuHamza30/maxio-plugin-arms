from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sale_rep_item_mrr import SaleRepItemMrr, SaleRepItemMrrDict


class ListSaleRepItem(SdkBaseModel):
    id: Optional[int] = UNSET
    full_name: Optional[str] = UNSET
    subscriptions_count: Optional[int] = UNSET
    mrr_data: Optional[dict[str, SaleRepItemMrr]] = UNSET
    test_mode: Optional[bool] = UNSET


class ListSaleRepItemDict(TypedDict):
    id: NotRequired[int]
    full_name: NotRequired[str]
    subscriptions_count: NotRequired[int]
    mrr_data: NotRequired[dict[str, SaleRepItemMrrDict]]
    test_mode: NotRequired[bool]
