from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SingleStringErrorResponse(SdkBaseModel):
    errors: Optional[str] = UNSET


class SingleStringErrorResponseDict(TypedDict):
    errors: NotRequired[str]
