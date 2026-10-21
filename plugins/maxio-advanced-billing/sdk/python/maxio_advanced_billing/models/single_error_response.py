from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SingleErrorResponse(SdkBaseModel):
    error: str


class SingleErrorResponseDict(TypedDict):
    error: str
