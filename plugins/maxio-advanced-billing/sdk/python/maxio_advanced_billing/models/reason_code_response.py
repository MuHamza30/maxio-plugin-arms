from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .reason_code import ReasonCode, ReasonCodeDict


class ReasonCodeResponse(SdkBaseModel):
    reason_code: ReasonCode


class ReasonCodeResponseDict(TypedDict):
    reason_code: ReasonCodeDict
