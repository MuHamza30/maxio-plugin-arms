from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .allocation_expiration_date import AllocationExpirationDate, AllocationExpirationDateDict


class UpdateAllocationExpirationDate(SdkBaseModel):
    allocation: Optional[AllocationExpirationDate] = UNSET


class UpdateAllocationExpirationDateDict(TypedDict):
    allocation: NotRequired[AllocationExpirationDateDict]
