from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class SubscriptionNote(SdkBaseModel):
    id: Optional[int] = UNSET
    body: Optional[str] = UNSET
    subscription_id: Optional[int] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET
    sticky: Optional[bool] = UNSET


class SubscriptionNoteDict(TypedDict):
    id: NotRequired[int]
    body: NotRequired[str]
    subscription_id: NotRequired[int]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    sticky: NotRequired[bool]
