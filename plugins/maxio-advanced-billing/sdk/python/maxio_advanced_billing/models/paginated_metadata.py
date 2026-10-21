from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .metadata import Metadata, MetadataDict


class PaginatedMetadata(SdkBaseModel):
    total_count: Optional[int] = UNSET
    current_page: Optional[int] = UNSET
    total_pages: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    metadata: Optional[list[Metadata]] = UNSET


class PaginatedMetadataDict(TypedDict):
    total_count: NotRequired[int]
    current_page: NotRequired[int]
    total_pages: NotRequired[int]
    per_page: NotRequired[int]
    metadata: NotRequired[list[MetadataDict]]
