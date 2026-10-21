from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription_component import SubscriptionComponent, SubscriptionComponentDict


class SubscriptionComponentResponse(SdkBaseModel):
    component: Optional[SubscriptionComponent] = UNSET


class SubscriptionComponentResponseDict(TypedDict):
    component: NotRequired[SubscriptionComponentDict]
