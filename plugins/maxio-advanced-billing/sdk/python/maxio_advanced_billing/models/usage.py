from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .unions.quantity1 import Quantity1, Quantity1Dict


class Usage(SdkBaseModel):
    id: Optional[int] = UNSET
    memo: OptionalNullable[str] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    price_point_id: Optional[int] = UNSET
    quantity: Optional[Quantity1] = UNSET
    overage_quantity: Optional[int] = UNSET
    component_id: Optional[int] = UNSET
    component_handle: Optional[str] = UNSET
    subscription_id: Optional[int] = UNSET


class UsageDict(TypedDict):
    id: NotRequired[int]
    memo: NotRequired[str | None]
    created_at: NotRequired[RFC3339DateTime]
    price_point_id: NotRequired[int]
    quantity: NotRequired[Quantity1Dict]
    overage_quantity: NotRequired[int]
    component_id: NotRequired[int]
    component_handle: NotRequired[str]
    subscription_id: NotRequired[int]
