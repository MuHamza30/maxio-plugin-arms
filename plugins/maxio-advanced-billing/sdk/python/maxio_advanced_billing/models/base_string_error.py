from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BaseStringError(SdkBaseModel):
    """The error is base if it is not directly associated with a single attribute."""

    base: Optional[list[str]] = UNSET


class BaseStringErrorDict(TypedDict):
    base: NotRequired[list[str]]
