from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Breakouts(SdkBaseModel):
    plan_amount_in_cents: Optional[int] = UNSET
    plan_amount_formatted: Optional[str] = UNSET
    usage_amount_in_cents: Optional[int] = UNSET
    usage_amount_formatted: Optional[str] = UNSET


class BreakoutsDict(TypedDict):
    plan_amount_in_cents: NotRequired[int]
    plan_amount_formatted: NotRequired[str]
    usage_amount_in_cents: NotRequired[int]
    usage_amount_formatted: NotRequired[str]
