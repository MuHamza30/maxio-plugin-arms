from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReplayWebhooksRequest(SdkBaseModel):
    ids: list[int]


class ReplayWebhooksRequestDict(TypedDict):
    ids: list[int]
