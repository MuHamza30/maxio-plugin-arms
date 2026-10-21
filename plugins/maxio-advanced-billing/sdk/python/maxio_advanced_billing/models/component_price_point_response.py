from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .component_price_point import ComponentPricePoint, ComponentPricePointDict


class ComponentPricePointResponse(SdkBaseModel):
    price_point: ComponentPricePoint


class ComponentPricePointResponseDict(TypedDict):
    price_point: ComponentPricePointDict
