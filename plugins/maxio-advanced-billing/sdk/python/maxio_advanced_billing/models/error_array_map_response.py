from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorArrayMapResponse(SdkBaseModel):
    errors: Optional[dict[str, Any]] = UNSET


class ErrorArrayMapResponseDict(TypedDict):
    errors: NotRequired[dict[str, Any]]
