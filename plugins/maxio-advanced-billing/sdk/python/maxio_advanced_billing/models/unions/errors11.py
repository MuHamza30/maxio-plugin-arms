from __future__ import annotations

from typing import TypeAlias

from ..subscription_group_members_array_error import (
    SubscriptionGroupMembersArrayError,
    SubscriptionGroupMembersArrayErrorDict,
)
from ..subscription_group_single_error import SubscriptionGroupSingleError, SubscriptionGroupSingleErrorDict

Errors11: TypeAlias = SubscriptionGroupMembersArrayError | SubscriptionGroupSingleError | str

Errors11Dict: TypeAlias = SubscriptionGroupMembersArrayErrorDict | SubscriptionGroupSingleErrorDict | str
