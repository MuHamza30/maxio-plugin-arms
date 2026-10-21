from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .segment import Segment, SegmentDict


class ListSegmentsResponse(SdkBaseModel):
    segments: Optional[list[Segment]] = UNSET


class ListSegmentsResponseDict(TypedDict):
    segments: NotRequired[list[SegmentDict]]
