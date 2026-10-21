from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_product_family import CreateProductFamily, CreateProductFamilyDict


class CreateProductFamilyRequest(SdkBaseModel):
    product_family: CreateProductFamily


class CreateProductFamilyRequestDict(TypedDict):
    product_family: CreateProductFamilyDict
