from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .breakouts import Breakouts, BreakoutsDict


class Mrr(SdkBaseModel):
    amount_in_cents: Optional[int] = UNSET
    amount_formatted: Optional[str] = UNSET
    currency: Optional[str] = UNSET
    currency_symbol: Optional[str] = UNSET
    breakouts: Optional[Breakouts] = UNSET
    at_time: Optional[RFC3339DateTime] = UNSET
    """ISO8601 timestamp"""


class MrrDict(TypedDict):
    amount_in_cents: NotRequired[int]
    amount_formatted: NotRequired[str]
    currency: NotRequired[str]
    currency_symbol: NotRequired[str]
    breakouts: NotRequired[BreakoutsDict]
    at_time: NotRequired[RFC3339DateTime]
