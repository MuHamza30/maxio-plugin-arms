from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pricing_scheme import PricingSchemeOrStr
from .price import Price, PriceDict


class OveragePricing(SdkBaseModel):
    pricing_scheme: PricingSchemeOrStr
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    prices: Optional[list[Price]] = UNSET


class OveragePricingDict(TypedDict):
    pricing_scheme: PricingSchemeOrStr
    prices: NotRequired[list[PriceDict]]
