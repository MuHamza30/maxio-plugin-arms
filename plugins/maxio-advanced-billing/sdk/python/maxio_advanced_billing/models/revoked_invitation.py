from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RevokedInvitation(SdkBaseModel):
    last_sent_at: Optional[str] = UNSET
    last_accepted_at: Optional[str] = UNSET
    uninvited_count: Optional[int] = UNSET


class RevokedInvitationDict(TypedDict):
    last_sent_at: NotRequired[str]
    last_accepted_at: NotRequired[str]
    uninvited_count: NotRequired[int]
