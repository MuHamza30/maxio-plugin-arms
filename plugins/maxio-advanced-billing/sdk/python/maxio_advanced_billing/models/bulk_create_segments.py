from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_segment import CreateSegment, CreateSegmentDict


class BulkCreateSegments(SdkBaseModel):
    segments: Optional[list[CreateSegment]] = UNSET


class BulkCreateSegmentsDict(TypedDict):
    segments: NotRequired[list[CreateSegmentDict]]
