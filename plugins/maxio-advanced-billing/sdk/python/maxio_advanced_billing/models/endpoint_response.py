from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .endpoint import Endpoint, EndpointDict


class EndpointResponse(SdkBaseModel):
    endpoint: Optional[Endpoint] = UNSET


class EndpointResponseDict(TypedDict):
    endpoint: NotRequired[EndpointDict]
