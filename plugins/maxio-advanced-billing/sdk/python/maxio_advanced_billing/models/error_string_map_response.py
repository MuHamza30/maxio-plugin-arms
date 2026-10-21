from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorStringMapResponse(SdkBaseModel):
    errors: Optional[dict[str, str]] = UNSET


class ErrorStringMapResponseDict(TypedDict):
    errors: NotRequired[dict[str, str]]
