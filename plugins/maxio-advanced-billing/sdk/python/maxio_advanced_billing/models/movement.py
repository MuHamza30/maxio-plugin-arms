from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .breakouts import Breakouts, BreakoutsDict
from .movement_line_item import MovementLineItem, MovementLineItemDict


class Movement(SdkBaseModel):
    timestamp: Optional[RFC3339DateTime] = UNSET
    amount_in_cents: Optional[int] = UNSET
    amount_formatted: Optional[str] = UNSET
    description: Optional[str] = UNSET
    category: Optional[str] = UNSET
    breakouts: Optional[Breakouts] = UNSET
    line_items: Optional[list[MovementLineItem]] = UNSET
    subscription_id: Optional[int] = UNSET
    subscriber_name: Optional[str] = UNSET


class MovementDict(TypedDict):
    timestamp: NotRequired[RFC3339DateTime]
    amount_in_cents: NotRequired[int]
    amount_formatted: NotRequired[str]
    description: NotRequired[str]
    category: NotRequired[str]
    breakouts: NotRequired[BreakoutsDict]
    line_items: NotRequired[list[MovementLineItemDict]]
    subscription_id: NotRequired[int]
    subscriber_name: NotRequired[str]
