from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .prepaid_usage_component import PrepaidUsageComponent, PrepaidUsageComponentDict


class CreatePrepaidComponent(SdkBaseModel):
    prepaid_usage_component: PrepaidUsageComponent


class CreatePrepaidComponentDict(TypedDict):
    prepaid_usage_component: PrepaidUsageComponentDict
