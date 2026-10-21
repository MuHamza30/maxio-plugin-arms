from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Endpoint(SdkBaseModel):
    id: Optional[int] = UNSET
    url: Optional[str] = UNSET
    site_id: Optional[int] = UNSET
    status: Optional[str] = UNSET
    webhook_subscriptions: Optional[list[str]] = UNSET


class EndpointDict(TypedDict):
    id: NotRequired[int]
    url: NotRequired[str]
    site_id: NotRequired[int]
    status: NotRequired[str]
    webhook_subscriptions: NotRequired[list[str]]
