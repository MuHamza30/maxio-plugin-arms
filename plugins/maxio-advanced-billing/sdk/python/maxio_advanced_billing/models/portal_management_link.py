from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class PortalManagementLink(SdkBaseModel):
    url: Optional[str] = UNSET
    fetch_count: Optional[int] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    new_link_available_at: Optional[RFC3339DateTime] = UNSET
    expires_at: Optional[RFC3339DateTime] = UNSET
    last_invite_sent_at: OptionalNullable[RFC3339DateTime] = UNSET


class PortalManagementLinkDict(TypedDict):
    url: NotRequired[str]
    fetch_count: NotRequired[int]
    created_at: NotRequired[RFC3339DateTime]
    new_link_available_at: NotRequired[RFC3339DateTime]
    expires_at: NotRequired[RFC3339DateTime]
    last_invite_sent_at: NotRequired[RFC3339DateTime | None]
