from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ErrorListResponse1(SdkBaseModel):
    """Error which contains list of messages."""

    errors: list[str]


class ErrorListResponse1Dict(TypedDict):
    errors: list[str]
