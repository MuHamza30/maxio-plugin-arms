from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .usage import Usage, UsageDict


class UsageResponse(SdkBaseModel):
    usage: Usage


class UsageResponseDict(TypedDict):
    usage: UsageDict
