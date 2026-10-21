from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .component_price_point_error_item import ComponentPricePointErrorItem, ComponentPricePointErrorItemDict


class ComponentPricePointError1(SdkBaseModel):
    errors: Optional[list[ComponentPricePointErrorItem]] = UNSET


class ComponentPricePointError1Dict(TypedDict):
    errors: NotRequired[list[ComponentPricePointErrorItemDict]]
