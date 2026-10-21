from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class AllocationExpirationDate(SdkBaseModel):
    expires_at: Optional[RFC3339DateTime] = UNSET


class AllocationExpirationDateDict(TypedDict):
    expires_at: NotRequired[RFC3339DateTime]
