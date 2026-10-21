from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .quantity_based_component import QuantityBasedComponent, QuantityBasedComponentDict


class CreateQuantityBasedComponent(SdkBaseModel):
    quantity_based_component: QuantityBasedComponent


class CreateQuantityBasedComponentDict(TypedDict):
    quantity_based_component: QuantityBasedComponentDict
