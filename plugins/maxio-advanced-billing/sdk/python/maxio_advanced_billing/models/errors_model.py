from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorsModel(SdkBaseModel):
    per_page: Optional[list[str]] = UNSET
    price_point: Optional[list[str]] = UNSET


class ErrorsModelDict(TypedDict):
    per_page: NotRequired[list[str]]
    price_point: NotRequired[list[str]]
