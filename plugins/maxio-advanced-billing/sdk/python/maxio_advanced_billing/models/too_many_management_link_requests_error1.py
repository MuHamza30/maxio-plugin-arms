from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .too_many_management_link_requests import TooManyManagementLinkRequests, TooManyManagementLinkRequestsDict


class TooManyManagementLinkRequestsError1(SdkBaseModel):
    errors: TooManyManagementLinkRequests


class TooManyManagementLinkRequestsError1Dict(TypedDict):
    errors: TooManyManagementLinkRequestsDict
