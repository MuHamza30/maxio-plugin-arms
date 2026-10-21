from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CountResponse(SdkBaseModel):
    count: Optional[int] = UNSET


class CountResponseDict(TypedDict):
    count: NotRequired[int]
