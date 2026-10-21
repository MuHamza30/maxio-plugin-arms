from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .segment import Segment, SegmentDict


class SegmentResponse(SdkBaseModel):
    segment: Optional[Segment] = UNSET


class SegmentResponseDict(TypedDict):
    segment: NotRequired[SegmentDict]
