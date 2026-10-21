from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SingleErrorResponse1(SdkBaseModel):
    error: str


class SingleErrorResponse1Dict(TypedDict):
    error: str
