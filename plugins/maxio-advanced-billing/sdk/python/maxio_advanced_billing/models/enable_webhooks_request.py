from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EnableWebhooksRequest(SdkBaseModel):
    webhooks_enabled: bool


class EnableWebhooksRequestDict(TypedDict):
    webhooks_enabled: bool
