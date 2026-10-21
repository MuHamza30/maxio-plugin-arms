from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.price_point import PricePoint, PricePointDict


class CreateComponentPricePointsRequest(SdkBaseModel):
    price_points: list[PricePoint]


class CreateComponentPricePointsRequestDict(TypedDict):
    price_points: list[PricePointDict]
