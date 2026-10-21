from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription_group_update_error import SubscriptionGroupUpdateError, SubscriptionGroupUpdateErrorDict


class SubscriptionGroupUpdateErrorResponse1(SdkBaseModel):
    errors: Optional[SubscriptionGroupUpdateError] = UNSET


class SubscriptionGroupUpdateErrorResponse1Dict(TypedDict):
    errors: NotRequired[SubscriptionGroupUpdateErrorDict]
