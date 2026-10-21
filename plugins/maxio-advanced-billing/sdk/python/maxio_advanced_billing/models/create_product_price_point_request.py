from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_product_price_point import CreateProductPricePoint, CreateProductPricePointDict


class CreateProductPricePointRequest(SdkBaseModel):
    price_point: CreateProductPricePoint


class CreateProductPricePointRequestDict(TypedDict):
    price_point: CreateProductPricePointDict
