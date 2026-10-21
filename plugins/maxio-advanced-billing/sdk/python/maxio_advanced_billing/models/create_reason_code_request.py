from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_reason_code import CreateReasonCode, CreateReasonCodeDict


class CreateReasonCodeRequest(SdkBaseModel):
    reason_code: CreateReasonCode


class CreateReasonCodeRequestDict(TypedDict):
    reason_code: CreateReasonCodeDict
