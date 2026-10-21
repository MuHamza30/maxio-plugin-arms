from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.group_target_type import GroupTargetTypeOrStr


class GroupTarget(SdkBaseModel):
    """Attributes of the target customer who will be the responsible payer of the created subscription. Required."""

    type_: GroupTargetTypeOrStr = Field(alias="type")
    """The type of object indicated by the id attribute."""

    id: Optional[int] = UNSET
    """The id of the target customer or subscription to group the existing subscription with. Ignored and should not be
    included if type is "self", "parent", or "eldest"."""


class GroupTargetDict(TypedDict):
    type_: GroupTargetTypeOrStr
    id: NotRequired[int]
