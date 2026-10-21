from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddCouponsRequest(SdkBaseModel):
    codes: Optional[list[str]] = UNSET


class AddCouponsRequestDict(TypedDict):
    codes: NotRequired[list[str]]
