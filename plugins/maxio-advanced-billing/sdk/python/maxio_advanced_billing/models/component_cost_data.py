from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .component_cost_data_rate_tier import ComponentCostDataRateTier, ComponentCostDataRateTierDict
from .enums.pricing_scheme import PricingSchemeOrStr


class ComponentCostData(SdkBaseModel):
    component_code_id: OptionalNullable[int] = UNSET
    price_point_id: Optional[int] = UNSET
    product_id: Optional[int] = UNSET
    quantity: Optional[str] = UNSET
    amount: Optional[str] = UNSET
    pricing_scheme: Optional[PricingSchemeOrStr] = UNSET
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    tiers: Optional[list[ComponentCostDataRateTier]] = UNSET


class ComponentCostDataDict(TypedDict):
    component_code_id: NotRequired[int | None]
    price_point_id: NotRequired[int]
    product_id: NotRequired[int]
    quantity: NotRequired[str]
    amount: NotRequired[str]
    pricing_scheme: NotRequired[PricingSchemeOrStr]
    tiers: NotRequired[list[ComponentCostDataRateTierDict]]
