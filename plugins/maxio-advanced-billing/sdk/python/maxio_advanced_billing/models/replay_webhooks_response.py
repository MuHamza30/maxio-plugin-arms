from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReplayWebhooksResponse(SdkBaseModel):
    status: Optional[str] = UNSET


class ReplayWebhooksResponseDict(TypedDict):
    status: NotRequired[str]
