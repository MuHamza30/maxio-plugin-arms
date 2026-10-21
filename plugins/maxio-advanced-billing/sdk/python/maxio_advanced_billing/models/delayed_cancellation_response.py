from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DelayedCancellationResponse(SdkBaseModel):
    message: Optional[str] = UNSET


class DelayedCancellationResponseDict(TypedDict):
    message: NotRequired[str]
