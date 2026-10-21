from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .renewal_preview_component import RenewalPreviewComponent, RenewalPreviewComponentDict


class RenewalPreviewRequest(SdkBaseModel):
    components: Optional[list[RenewalPreviewComponent]] = UNSET
    """(Optional) Array of component definitions to preview. Providing any component definitions here will override the
    actual components on the subscription (and their quantities), and the billing preview will contain only these
    components (in addition to any product base fees)."""


class RenewalPreviewRequestDict(TypedDict):
    components: NotRequired[list[RenewalPreviewComponentDict]]
