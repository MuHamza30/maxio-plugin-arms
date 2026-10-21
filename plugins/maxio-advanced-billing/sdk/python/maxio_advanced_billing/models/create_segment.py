from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_or_update_segment_price import CreateOrUpdateSegmentPrice, CreateOrUpdateSegmentPriceDict
from .enums.pricing_scheme import PricingSchemeOrStr
from .unions.segment_property1_value import SegmentProperty1Value, SegmentProperty1ValueDict
from .unions.segment_property2_value import SegmentProperty2Value, SegmentProperty2ValueDict
from .unions.segment_property3_value import SegmentProperty3Value, SegmentProperty3ValueDict
from .unions.segment_property4_value import SegmentProperty4Value, SegmentProperty4ValueDict


class CreateSegment(SdkBaseModel):
    segment_property_1_value: Optional[SegmentProperty1Value] = UNSET
    """A value that will occur in your events that you want to bill upon. The type of the value depends on the property
    type in the related event based billing metric."""

    segment_property_2_value: Optional[SegmentProperty2Value] = UNSET
    """A value that will occur in your events that you want to bill upon. The type of the value depends on the property
    type in the related event based billing metric."""

    segment_property_3_value: Optional[SegmentProperty3Value] = UNSET
    """A value that will occur in your events that you want to bill upon. The type of the value depends on the property
    type in the related event based billing metric."""

    segment_property_4_value: Optional[SegmentProperty4Value] = UNSET
    """A value that will occur in your events that you want to bill upon. The type of the value depends on the property
    type in the related event based billing metric."""

    pricing_scheme: PricingSchemeOrStr
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    prices: Optional[list[CreateOrUpdateSegmentPrice]] = UNSET


class CreateSegmentDict(TypedDict):
    segment_property_1_value: NotRequired[SegmentProperty1ValueDict]
    segment_property_2_value: NotRequired[SegmentProperty2ValueDict]
    segment_property_3_value: NotRequired[SegmentProperty3ValueDict]
    segment_property_4_value: NotRequired[SegmentProperty4ValueDict]
    pricing_scheme: PricingSchemeOrStr
    prices: NotRequired[list[CreateOrUpdateSegmentPriceDict]]
