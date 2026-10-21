from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PrepaidUsageAllocationDetail(SdkBaseModel):
    allocation_id: Optional[int] = UNSET
    charge_id: Optional[int] = UNSET
    usage_quantity: Optional[int] = UNSET


class PrepaidUsageAllocationDetailDict(TypedDict):
    allocation_id: NotRequired[int]
    charge_id: NotRequired[int]
    usage_quantity: NotRequired[int]
