from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .product_price_point import ProductPricePoint, ProductPricePointDict


class ProductPricePointResponse(SdkBaseModel):
    price_point: ProductPricePoint


class ProductPricePointResponseDict(TypedDict):
    price_point: ProductPricePointDict
