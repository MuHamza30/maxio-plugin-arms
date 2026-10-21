from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.allocated_quantity import AllocatedQuantity, AllocatedQuantityDict


class ComponentAllocationChange(SdkBaseModel):
    previous_allocation: int
    new_allocation: int
    component_id: int
    component_handle: str
    memo: str
    allocation_id: int
    allocated_quantity: Optional[AllocatedQuantity] = UNSET


class ComponentAllocationChangeDict(TypedDict):
    previous_allocation: int
    new_allocation: int
    component_id: int
    component_handle: str
    memo: str
    allocation_id: int
    allocated_quantity: NotRequired[AllocatedQuantityDict]
