from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_usage import CreateUsage, CreateUsageDict


class CreateUsageRequest(SdkBaseModel):
    usage: CreateUsage


class CreateUsageRequestDict(TypedDict):
    usage: CreateUsageDict
