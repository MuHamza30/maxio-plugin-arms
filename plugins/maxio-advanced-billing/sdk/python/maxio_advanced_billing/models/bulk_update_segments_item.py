from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_or_update_segment_price import CreateOrUpdateSegmentPrice, CreateOrUpdateSegmentPriceDict
from .enums.pricing_scheme import PricingSchemeOrStr


class BulkUpdateSegmentsItem(SdkBaseModel):
    id: int
    """The ID of the segment you want to update."""

    pricing_scheme: PricingSchemeOrStr
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    prices: list[CreateOrUpdateSegmentPrice]


class BulkUpdateSegmentsItemDict(TypedDict):
    id: int
    pricing_scheme: PricingSchemeOrStr
    prices: list[CreateOrUpdateSegmentPriceDict]
