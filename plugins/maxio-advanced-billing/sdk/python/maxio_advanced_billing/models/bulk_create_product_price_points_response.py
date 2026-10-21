from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .product_price_point import ProductPricePoint, ProductPricePointDict


class BulkCreateProductPricePointsResponse(SdkBaseModel):
    price_points: Optional[list[ProductPricePoint]] = UNSET


class BulkCreateProductPricePointsResponseDict(TypedDict):
    price_points: NotRequired[list[ProductPricePointDict]]
