from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .send_email import SendEmail, SendEmailDict


class AvailableActions(SdkBaseModel):
    send_email: Optional[SendEmail] = UNSET


class AvailableActionsDict(TypedDict):
    send_email: NotRequired[SendEmailDict]
