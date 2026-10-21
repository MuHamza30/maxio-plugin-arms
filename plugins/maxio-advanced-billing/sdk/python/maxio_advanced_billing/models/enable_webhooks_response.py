from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EnableWebhooksResponse(SdkBaseModel):
    webhooks_enabled: Optional[bool] = UNSET


class EnableWebhooksResponseDict(TypedDict):
    webhooks_enabled: NotRequired[bool]
