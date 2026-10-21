from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_metadata import CreateMetadata, CreateMetadataDict


class CreateMetadataRequest(SdkBaseModel):
    metadata: list[CreateMetadata]


class CreateMetadataRequestDict(TypedDict):
    metadata: list[CreateMetadataDict]
