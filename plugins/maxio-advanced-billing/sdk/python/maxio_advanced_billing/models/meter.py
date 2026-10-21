from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meter(SdkBaseModel):
    """The metering meter this wallet is paired with, or ``null`` for a wallet with no meter. Set on create and
    immutable afterward."""

    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    handle: Optional[str] = UNSET
    conversion_rate: Optional[str] = UNSET
    """How many wallet units one meter unit is worth, as a decimal string. Defaults to ``"1.0"``."""


class MeterDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    handle: NotRequired[str]
    conversion_rate: NotRequired[str]
