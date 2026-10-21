from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorArrayMapResponse1(SdkBaseModel):
    errors: Optional[dict[str, Any]] = UNSET


class ErrorArrayMapResponse1Dict(TypedDict):
    errors: NotRequired[dict[str, Any]]
