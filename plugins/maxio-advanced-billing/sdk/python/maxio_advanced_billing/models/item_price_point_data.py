from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemPricePointData(SdkBaseModel):
    id: Optional[int] = UNSET
    handle: Optional[str] = UNSET
    name: Optional[str] = UNSET


class ItemPricePointDataDict(TypedDict):
    id: NotRequired[int]
    handle: NotRequired[str]
    name: NotRequired[str]
