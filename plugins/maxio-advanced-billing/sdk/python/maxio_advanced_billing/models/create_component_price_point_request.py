from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.price_point import PricePoint, PricePointDict


class CreateComponentPricePointRequest(SdkBaseModel):
    price_point: PricePoint


class CreateComponentPricePointRequestDict(TypedDict):
    price_point: PricePointDict
