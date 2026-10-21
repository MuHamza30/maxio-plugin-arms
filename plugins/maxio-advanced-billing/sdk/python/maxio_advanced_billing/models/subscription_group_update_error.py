from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubscriptionGroupUpdateError(SdkBaseModel):
    members: Optional[list[str]] = UNSET


class SubscriptionGroupUpdateErrorDict(TypedDict):
    members: NotRequired[list[str]]
