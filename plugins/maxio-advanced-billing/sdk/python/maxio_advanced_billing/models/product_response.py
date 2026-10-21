from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .product import Product, ProductDict


class ProductResponse(SdkBaseModel):
    product: Product


class ProductResponseDict(TypedDict):
    product: ProductDict
