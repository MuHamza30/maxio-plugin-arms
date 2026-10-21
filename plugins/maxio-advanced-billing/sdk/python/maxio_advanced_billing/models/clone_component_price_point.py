from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CloneComponentPricePoint(SdkBaseModel):
    name: str
    handle: Optional[str] = UNSET


class CloneComponentPricePointDict(TypedDict):
    name: str
    handle: NotRequired[str]
