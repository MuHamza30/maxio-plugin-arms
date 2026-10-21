from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .component_price_point import ComponentPricePoint, ComponentPricePointDict


class ListComponentsPricePointsResponse(SdkBaseModel):
    price_points: list[ComponentPricePoint]


class ListComponentsPricePointsResponseDict(TypedDict):
    price_points: list[ComponentPricePointDict]
