from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .update_component_price_point import UpdateComponentPricePoint, UpdateComponentPricePointDict


class UpdateComponentPricePointRequest(SdkBaseModel):
    price_point: Optional[UpdateComponentPricePoint] = UNSET


class UpdateComponentPricePointRequestDict(TypedDict):
    price_point: NotRequired[UpdateComponentPricePointDict]
