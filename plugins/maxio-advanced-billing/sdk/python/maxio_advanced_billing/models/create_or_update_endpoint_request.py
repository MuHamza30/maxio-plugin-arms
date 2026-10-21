from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_or_update_endpoint import CreateOrUpdateEndpoint, CreateOrUpdateEndpointDict


class CreateOrUpdateEndpointRequest(SdkBaseModel):
    """Used to Create or Update Endpoint."""

    endpoint: CreateOrUpdateEndpoint
    """Used to Create or Update Endpoint."""


class CreateOrUpdateEndpointRequestDict(TypedDict):
    endpoint: CreateOrUpdateEndpointDict
