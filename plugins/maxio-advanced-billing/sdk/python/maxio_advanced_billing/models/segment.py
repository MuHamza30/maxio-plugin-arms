from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.pricing_scheme import PricingSchemeOrStr
from .segment_price import SegmentPrice, SegmentPriceDict
from .unions.segment_property1_value1 import SegmentProperty1Value1, SegmentProperty1Value1Dict
from .unions.segment_property2_value1 import SegmentProperty2Value1, SegmentProperty2Value1Dict
from .unions.segment_property3_value1 import SegmentProperty3Value1, SegmentProperty3Value1Dict
from .unions.segment_property4_value1 import SegmentProperty4Value1, SegmentProperty4Value1Dict


class Segment(SdkBaseModel):
    id: Optional[int] = UNSET
    component_id: Optional[int] = UNSET
    price_point_id: Optional[int] = UNSET
    event_based_billing_metric_id: Optional[int] = UNSET
    pricing_scheme: Optional[PricingSchemeOrStr] = UNSET
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    segment_property_1_value: Optional[SegmentProperty1Value1] = UNSET
    segment_property_2_value: Optional[SegmentProperty2Value1] = UNSET
    segment_property_3_value: Optional[SegmentProperty3Value1] = UNSET
    segment_property_4_value: Optional[SegmentProperty4Value1] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET
    prices: Optional[list[SegmentPrice]] = UNSET


class SegmentDict(TypedDict):
    id: NotRequired[int]
    component_id: NotRequired[int]
    price_point_id: NotRequired[int]
    event_based_billing_metric_id: NotRequired[int]
    pricing_scheme: NotRequired[PricingSchemeOrStr]
    segment_property_1_value: NotRequired[SegmentProperty1Value1Dict]
    segment_property_2_value: NotRequired[SegmentProperty2Value1Dict]
    segment_property_3_value: NotRequired[SegmentProperty3Value1Dict]
    segment_property_4_value: NotRequired[SegmentProperty4Value1Dict]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    prices: NotRequired[list[SegmentPriceDict]]
