from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubscriptionGroupMembersArrayError(SdkBaseModel):
    members: list[str]


class SubscriptionGroupMembersArrayErrorDict(TypedDict):
    members: list[str]
