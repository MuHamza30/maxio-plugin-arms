from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SendEmail(SdkBaseModel):
    can_execute: bool
    url: str


class SendEmailDict(TypedDict):
    can_execute: bool
    url: str
