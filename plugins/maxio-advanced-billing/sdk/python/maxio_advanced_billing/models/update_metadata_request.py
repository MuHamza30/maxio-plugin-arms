from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .update_metadata import UpdateMetadata, UpdateMetadataDict


class UpdateMetadataRequest(SdkBaseModel):
    metadata: Optional[UpdateMetadata] = UNSET


class UpdateMetadataRequestDict(TypedDict):
    metadata: NotRequired[UpdateMetadataDict]
