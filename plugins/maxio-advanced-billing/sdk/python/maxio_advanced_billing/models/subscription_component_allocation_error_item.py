from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubscriptionComponentAllocationErrorItem(SdkBaseModel):
    kind: Optional[str] = UNSET
    message: Optional[str] = UNSET


class SubscriptionComponentAllocationErrorItemDict(TypedDict):
    kind: NotRequired[str]
    message: NotRequired[str]
