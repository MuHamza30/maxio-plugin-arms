from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_product_price_point import CreateProductPricePoint, CreateProductPricePointDict


class BulkCreateProductPricePointsRequest(SdkBaseModel):
    price_points: list[CreateProductPricePoint]


class BulkCreateProductPricePointsRequestDict(TypedDict):
    price_points: list[CreateProductPricePointDict]
