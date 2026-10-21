from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ErrorListResponse(SdkBaseModel):
    """Error which contains list of messages."""

    errors: list[str]


class ErrorListResponseDict(TypedDict):
    errors: list[str]
