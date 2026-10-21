from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .renewal_preview import RenewalPreview, RenewalPreviewDict


class RenewalPreviewResponse(SdkBaseModel):
    renewal_preview: RenewalPreview


class RenewalPreviewResponseDict(TypedDict):
    renewal_preview: RenewalPreviewDict
