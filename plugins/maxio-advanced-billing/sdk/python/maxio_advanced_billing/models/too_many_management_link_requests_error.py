from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .too_many_management_link_requests import TooManyManagementLinkRequests, TooManyManagementLinkRequestsDict


class TooManyManagementLinkRequestsError(SdkBaseModel):
    errors: TooManyManagementLinkRequests


class TooManyManagementLinkRequestsErrorDict(TypedDict):
    errors: TooManyManagementLinkRequestsDict
