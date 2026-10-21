from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateSubscriptionGroup(SdkBaseModel):
    member_ids: Optional[list[int]] = UNSET


class UpdateSubscriptionGroupDict(TypedDict):
    member_ids: NotRequired[list[int]]
