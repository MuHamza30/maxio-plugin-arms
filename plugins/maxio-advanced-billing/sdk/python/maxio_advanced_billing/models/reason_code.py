from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ReasonCode(SdkBaseModel):
    id: Optional[int] = UNSET
    site_id: Optional[int] = UNSET
    code: Optional[str] = UNSET
    description: Optional[str] = UNSET
    position: Optional[int] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET


class ReasonCodeDict(TypedDict):
    id: NotRequired[int]
    site_id: NotRequired[int]
    code: NotRequired[str]
    description: NotRequired[str]
    position: NotRequired[int]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
