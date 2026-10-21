from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MrrMovement(SdkBaseModel):
    amount: Optional[int] = UNSET
    category: Optional[str] = UNSET
    subscriber_delta: Optional[int] = UNSET
    lead_delta: Optional[int] = UNSET


class MrrMovementDict(TypedDict):
    amount: NotRequired[int]
    category: NotRequired[str]
    subscriber_delta: NotRequired[int]
    lead_delta: NotRequired[int]
