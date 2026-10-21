from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ComponentPricePointErrorItem(SdkBaseModel):
    component_id: Optional[int] = UNSET
    message: Optional[str] = UNSET
    price_point: Optional[int] = UNSET


class ComponentPricePointErrorItemDict(TypedDict):
    component_id: NotRequired[int]
    message: NotRequired[str]
    price_point: NotRequired[int]
