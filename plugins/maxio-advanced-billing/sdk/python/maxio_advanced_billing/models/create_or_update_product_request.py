from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_or_update_product import CreateOrUpdateProduct, CreateOrUpdateProductDict


class CreateOrUpdateProductRequest(SdkBaseModel):
    product: CreateOrUpdateProduct


class CreateOrUpdateProductRequestDict(TypedDict):
    product: CreateOrUpdateProductDict
