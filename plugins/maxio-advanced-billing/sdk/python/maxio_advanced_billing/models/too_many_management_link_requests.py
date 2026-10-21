from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class TooManyManagementLinkRequests(SdkBaseModel):
    error: str
    new_link_available_at: RFC3339DateTime


class TooManyManagementLinkRequestsDict(TypedDict):
    error: str
    new_link_available_at: RFC3339DateTime
