from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .product_family import ProductFamily, ProductFamilyDict


class ProductFamilyResponse(SdkBaseModel):
    product_family: Optional[ProductFamily] = UNSET


class ProductFamilyResponseDict(TypedDict):
    product_family: NotRequired[ProductFamilyDict]
