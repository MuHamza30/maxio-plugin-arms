from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .product_price_point_errors import ProductPricePointErrors, ProductPricePointErrorsDict


class ProductPricePointErrorResponse(SdkBaseModel):
    errors: ProductPricePointErrors


class ProductPricePointErrorResponseDict(TypedDict):
    errors: ProductPricePointErrorsDict
