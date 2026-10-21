from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auto_resume import AutoResume, AutoResumeDict


class PauseRequest(SdkBaseModel):
    """Allows you to pause a Subscription."""

    hold: Optional[AutoResume] = UNSET


class PauseRequestDict(TypedDict):
    hold: NotRequired[AutoResumeDict]
