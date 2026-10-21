from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListSegmentsFilter(SdkBaseModel):
    segment_property_1_value: Optional[str] = UNSET
    """The value passed here would be used to filter segments. Pass a value related to ``segment_property_1`` on
    attached Metric. If empty string is passed, this filter would be rejected. Use in query
    ``filter[segment_property_1_value]=EU``."""

    segment_property_2_value: Optional[str] = UNSET
    """The value passed here would be used to filter segments. Pass a value related to ``segment_property_2`` on
    attached Metric. If empty string is passed, this filter would be rejected."""

    segment_property_3_value: Optional[str] = UNSET
    """The value passed here would be used to filter segments. Pass a value related to ``segment_property_3`` on
    attached Metric. If empty string is passed, this filter would be rejected."""

    segment_property_4_value: Optional[str] = UNSET
    """The value passed here would be used to filter segments. Pass a value related to ``segment_property_4`` on
    attached Metric. If empty string is passed, this filter would be rejected."""


class ListSegmentsFilterDict(TypedDict):
    segment_property_1_value: NotRequired[str]
    segment_property_2_value: NotRequired[str]
    segment_property_3_value: NotRequired[str]
    segment_property_4_value: NotRequired[str]
