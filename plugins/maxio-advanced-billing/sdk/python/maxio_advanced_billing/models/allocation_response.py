from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .allocation import Allocation, AllocationDict


class AllocationResponse(SdkBaseModel):
    allocation: Optional[Allocation] = UNSET


class AllocationResponseDict(TypedDict):
    allocation: NotRequired[AllocationDict]
