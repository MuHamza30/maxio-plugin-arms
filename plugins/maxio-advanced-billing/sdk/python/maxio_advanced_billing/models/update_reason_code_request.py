from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_reason_code import UpdateReasonCode, UpdateReasonCodeDict


class UpdateReasonCodeRequest(SdkBaseModel):
    reason_code: UpdateReasonCode


class UpdateReasonCodeRequestDict(TypedDict):
    reason_code: UpdateReasonCodeDict
