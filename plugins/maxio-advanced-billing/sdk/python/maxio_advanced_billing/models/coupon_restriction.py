from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.restriction_type import RestrictionTypeOrStr


class CouponRestriction(SdkBaseModel):
    id: Optional[int] = UNSET
    item_type: Optional[RestrictionTypeOrStr] = UNSET
    item_id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    handle: OptionalNullable[str] = UNSET


class CouponRestrictionDict(TypedDict):
    id: NotRequired[int]
    item_type: NotRequired[RestrictionTypeOrStr]
    item_id: NotRequired[int]
    name: NotRequired[str]
    handle: NotRequired[str | None]
