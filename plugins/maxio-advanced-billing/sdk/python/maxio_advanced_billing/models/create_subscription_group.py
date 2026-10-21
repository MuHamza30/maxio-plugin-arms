from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateSubscriptionGroup(SdkBaseModel):
    subscription_id: int
    member_ids: Optional[list[int]] = UNSET


class CreateSubscriptionGroupDict(TypedDict):
    subscription_id: int
    member_ids: NotRequired[list[int]]
