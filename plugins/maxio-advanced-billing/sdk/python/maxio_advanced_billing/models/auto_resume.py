from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class AutoResume(SdkBaseModel):
    automatically_resume_at: OptionalNullable[RFC3339DateTime] = UNSET


class AutoResumeDict(TypedDict):
    automatically_resume_at: NotRequired[RFC3339DateTime | None]
