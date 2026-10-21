from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListMrrFilter(SdkBaseModel):
    subscription_ids: Optional[list[int]] = UNSET
    """Submit ids in order to limit results. Use in query: ``filter[subscription_ids]=1,2,3``."""


class ListMrrFilterDict(TypedDict):
    subscription_ids: NotRequired[list[int]]
