from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CouponSubcodesResponse(SdkBaseModel):
    created_codes: Optional[list[str]] = UNSET
    duplicate_codes: Optional[list[str]] = UNSET
    invalid_codes: Optional[list[str]] = UNSET


class CouponSubcodesResponseDict(TypedDict):
    created_codes: NotRequired[list[str]]
    duplicate_codes: NotRequired[list[str]]
    invalid_codes: NotRequired[list[str]]
