from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_segment import UpdateSegment, UpdateSegmentDict


class UpdateSegmentRequest(SdkBaseModel):
    segment: UpdateSegment


class UpdateSegmentRequestDict(TypedDict):
    segment: UpdateSegmentDict
