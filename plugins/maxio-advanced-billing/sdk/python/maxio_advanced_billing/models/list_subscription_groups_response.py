from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_subscription_groups_item import ListSubscriptionGroupsItem, ListSubscriptionGroupsItemDict
from .list_subscription_groups_meta import ListSubscriptionGroupsMeta, ListSubscriptionGroupsMetaDict


class ListSubscriptionGroupsResponse(SdkBaseModel):
    subscription_groups: Optional[list[ListSubscriptionGroupsItem]] = UNSET
    meta: Optional[ListSubscriptionGroupsMeta] = UNSET


class ListSubscriptionGroupsResponseDict(TypedDict):
    subscription_groups: NotRequired[list[ListSubscriptionGroupsItemDict]]
    meta: NotRequired[ListSubscriptionGroupsMetaDict]
