from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DunningStepData(SdkBaseModel):
    day_threshold: int
    action: str
    email_body: OptionalNullable[str] = UNSET
    email_subject: OptionalNullable[str] = UNSET
    send_email: bool
    send_bcc_email: bool
    send_sms: bool
    sms_body: OptionalNullable[str] = UNSET


class DunningStepDataDict(TypedDict):
    day_threshold: int
    action: str
    email_body: NotRequired[str | None]
    email_subject: NotRequired[str | None]
    send_email: bool
    send_bcc_email: bool
    send_sms: bool
    sms_body: NotRequired[str | None]
