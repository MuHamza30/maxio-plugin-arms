from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_segment import CreateSegment, CreateSegmentDict


class CreateSegmentRequest(SdkBaseModel):
    segment: CreateSegment


class CreateSegmentRequestDict(TypedDict):
    segment: CreateSegmentDict
