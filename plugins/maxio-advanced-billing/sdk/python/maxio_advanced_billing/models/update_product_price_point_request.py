from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_product_price_point import UpdateProductPricePoint, UpdateProductPricePointDict


class UpdateProductPricePointRequest(SdkBaseModel):
    price_point: UpdateProductPricePoint


class UpdateProductPricePointRequestDict(TypedDict):
    price_point: UpdateProductPricePointDict
