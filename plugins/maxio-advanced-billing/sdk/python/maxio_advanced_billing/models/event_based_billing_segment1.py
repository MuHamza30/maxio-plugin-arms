from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .event_based_billing_segment_error import EventBasedBillingSegmentError, EventBasedBillingSegmentErrorDict


class EventBasedBillingSegment1(SdkBaseModel):
    errors: EventBasedBillingSegmentError


class EventBasedBillingSegment1Dict(TypedDict):
    errors: EventBasedBillingSegmentErrorDict
