from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_or_update_segment_price import CreateOrUpdateSegmentPrice, CreateOrUpdateSegmentPriceDict
from .enums.pricing_scheme import PricingSchemeOrStr


class UpdateSegment(SdkBaseModel):
    pricing_scheme: PricingSchemeOrStr
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    prices: Optional[list[CreateOrUpdateSegmentPrice]] = UNSET


class UpdateSegmentDict(TypedDict):
    pricing_scheme: PricingSchemeOrStr
    prices: NotRequired[list[CreateOrUpdateSegmentPriceDict]]
