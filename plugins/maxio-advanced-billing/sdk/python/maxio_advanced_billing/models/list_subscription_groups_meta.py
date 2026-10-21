from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListSubscriptionGroupsMeta(SdkBaseModel):
    current_page: Optional[int] = UNSET
    total_count: Optional[int] = UNSET


class ListSubscriptionGroupsMetaDict(TypedDict):
    current_page: NotRequired[int]
    total_count: NotRequired[int]
