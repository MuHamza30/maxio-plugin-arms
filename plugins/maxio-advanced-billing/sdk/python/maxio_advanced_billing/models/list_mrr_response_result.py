from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .movement import Movement, MovementDict


class ListMrrResponseResult(SdkBaseModel):
    page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    total_pages: Optional[int] = UNSET
    total_entries: Optional[int] = UNSET
    currency: Optional[str] = UNSET
    currency_symbol: Optional[str] = UNSET
    movements: Optional[list[Movement]] = UNSET


class ListMrrResponseResultDict(TypedDict):
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_pages: NotRequired[int]
    total_entries: NotRequired[int]
    currency: NotRequired[str]
    currency_symbol: NotRequired[str]
    movements: NotRequired[list[MovementDict]]
