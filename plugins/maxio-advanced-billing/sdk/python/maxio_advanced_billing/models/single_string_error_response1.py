from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SingleStringErrorResponse1(SdkBaseModel):
    errors: Optional[str] = UNSET


class SingleStringErrorResponse1Dict(TypedDict):
    errors: NotRequired[str]
