from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_update_segments_item import BulkUpdateSegmentsItem, BulkUpdateSegmentsItemDict


class BulkUpdateSegments(SdkBaseModel):
    segments: Optional[list[BulkUpdateSegmentsItem]] = UNSET


class BulkUpdateSegmentsDict(TypedDict):
    segments: NotRequired[list[BulkUpdateSegmentsItemDict]]
