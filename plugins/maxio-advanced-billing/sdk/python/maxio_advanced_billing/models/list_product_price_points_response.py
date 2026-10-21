from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .product_price_point import ProductPricePoint, ProductPricePointDict


class ListProductPricePointsResponse(SdkBaseModel):
    price_points: list[ProductPricePoint]


class ListProductPricePointsResponseDict(TypedDict):
    price_points: list[ProductPricePointDict]
