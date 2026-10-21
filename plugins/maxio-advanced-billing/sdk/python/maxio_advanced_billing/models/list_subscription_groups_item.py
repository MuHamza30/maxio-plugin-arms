from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.group_type import GroupTypeOrStr
from .subscription_group_balances import SubscriptionGroupBalances, SubscriptionGroupBalancesDict


class ListSubscriptionGroupsItem(SdkBaseModel):
    uid: Optional[str] = UNSET
    scheme: Optional[int] = UNSET
    customer_id: Optional[int] = UNSET
    payment_profile_id: Optional[int] = UNSET
    subscription_ids: Optional[list[int]] = UNSET
    primary_subscription_id: Optional[int] = UNSET
    next_assessment_at: Optional[RFC3339DateTime] = UNSET
    state: Optional[str] = UNSET
    cancel_at_end_of_period: Optional[bool] = UNSET
    account_balances: Optional[SubscriptionGroupBalances] = UNSET
    group_type: Optional[GroupTypeOrStr] = UNSET


class ListSubscriptionGroupsItemDict(TypedDict):
    uid: NotRequired[str]
    scheme: NotRequired[int]
    customer_id: NotRequired[int]
    payment_profile_id: NotRequired[int]
    subscription_ids: NotRequired[list[int]]
    primary_subscription_id: NotRequired[int]
    next_assessment_at: NotRequired[RFC3339DateTime]
    state: NotRequired[str]
    cancel_at_end_of_period: NotRequired[bool]
    account_balances: NotRequired[SubscriptionGroupBalancesDict]
    group_type: NotRequired[GroupTypeOrStr]
