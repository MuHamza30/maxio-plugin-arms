from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .metafield import Metafield, MetafieldDict


class ListMetafieldsResponse(SdkBaseModel):
    total_count: Optional[int] = UNSET
    current_page: Optional[int] = UNSET
    total_pages: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    metafields: Optional[list[Metafield]] = UNSET


class ListMetafieldsResponseDict(TypedDict):
    total_count: NotRequired[int]
    current_page: NotRequired[int]
    total_pages: NotRequired[int]
    per_page: NotRequired[int]
    metafields: NotRequired[list[MetafieldDict]]
