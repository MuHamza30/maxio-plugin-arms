from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .allocation_preview import AllocationPreview, AllocationPreviewDict


class AllocationPreviewResponse(SdkBaseModel):
    allocation_preview: AllocationPreview


class AllocationPreviewResponseDict(TypedDict):
    allocation_preview: AllocationPreviewDict
