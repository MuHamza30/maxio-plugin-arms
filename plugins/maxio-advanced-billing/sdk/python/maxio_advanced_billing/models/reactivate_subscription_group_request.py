from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReactivateSubscriptionGroupRequest(SdkBaseModel):
    resume: Optional[bool] = UNSET
    resume_members: Optional[bool] = UNSET


class ReactivateSubscriptionGroupRequestDict(TypedDict):
    resume: NotRequired[bool]
    resume_members: NotRequired[bool]
