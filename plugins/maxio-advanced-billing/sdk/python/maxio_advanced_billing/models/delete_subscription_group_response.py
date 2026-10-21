from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeleteSubscriptionGroupResponse(SdkBaseModel):
    uid: Optional[str] = UNSET
    deleted: Optional[bool] = UNSET


class DeleteSubscriptionGroupResponseDict(TypedDict):
    uid: NotRequired[str]
    deleted: NotRequired[bool]
