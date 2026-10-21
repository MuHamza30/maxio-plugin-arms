from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ResentInvitation(SdkBaseModel):
    last_sent_at: Optional[str] = UNSET
    last_accepted_at: Optional[str] = UNSET
    send_invite_link_text: Optional[str] = UNSET
    uninvited_count: Optional[int] = UNSET
    last_invite_sent_at: Optional[RFC3339DateTime] = UNSET
    last_invite_accepted_at: Optional[RFC3339DateTime] = UNSET


class ResentInvitationDict(TypedDict):
    last_sent_at: NotRequired[str]
    last_accepted_at: NotRequired[str]
    send_invite_link_text: NotRequired[str]
    uninvited_count: NotRequired[int]
    last_invite_sent_at: NotRequired[RFC3339DateTime]
    last_invite_accepted_at: NotRequired[RFC3339DateTime]
