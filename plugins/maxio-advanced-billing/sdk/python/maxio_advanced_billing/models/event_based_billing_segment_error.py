from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EventBasedBillingSegmentError(SdkBaseModel):
    segments: dict[str, Any]
    """The key of the object would be a number (an index in the request array) where the error occurred. In the value
    object, the key represents the field and the value is an array with error messages. In most cases, this object would
    contain just one key."""


class EventBasedBillingSegmentErrorDict(TypedDict):
    segments: dict[str, Any]
