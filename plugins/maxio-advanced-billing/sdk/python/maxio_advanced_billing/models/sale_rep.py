from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sale_rep_subscription import SaleRepSubscription, SaleRepSubscriptionDict


class SaleRep(SdkBaseModel):
    id: Optional[int] = UNSET
    full_name: Optional[str] = UNSET
    subscriptions_count: Optional[int] = UNSET
    test_mode: Optional[bool] = UNSET
    subscriptions: Optional[list[SaleRepSubscription]] = UNSET


class SaleRepDict(TypedDict):
    id: NotRequired[int]
    full_name: NotRequired[str]
    subscriptions_count: NotRequired[int]
    test_mode: NotRequired[bool]
    subscriptions: NotRequired[list[SaleRepSubscriptionDict]]
