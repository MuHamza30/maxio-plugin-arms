from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .component_custom_price import ComponentCustomPrice, ComponentCustomPriceDict
from .enums.pricing_scheme import PricingSchemeOrStr
from .price import Price, PriceDict


class SubscriptionGroupComponentCustomPrice(SdkBaseModel):
    """Used in place of ``price_point_id`` to define a custom price point unique to the subscription. You still need to
    provide ``component_id``."""

    pricing_scheme: Optional[PricingSchemeOrStr] = UNSET
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    prices: Optional[list[Price]] = UNSET
    overage_pricing: Optional[list[ComponentCustomPrice]] = UNSET


class SubscriptionGroupComponentCustomPriceDict(TypedDict):
    pricing_scheme: NotRequired[PricingSchemeOrStr]
    prices: NotRequired[list[PriceDict]]
    overage_pricing: NotRequired[list[ComponentCustomPriceDict]]
