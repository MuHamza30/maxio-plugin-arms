from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CouponSubcodes(SdkBaseModel):
    codes: Optional[list[str]] = UNSET


class CouponSubcodesDict(TypedDict):
    codes: NotRequired[list[str]]
