from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .clone_component_price_point import CloneComponentPricePoint, CloneComponentPricePointDict


class CloneComponentPricePointRequest(SdkBaseModel):
    price_point: CloneComponentPricePoint


class CloneComponentPricePointRequestDict(TypedDict):
    price_point: CloneComponentPricePointDict
