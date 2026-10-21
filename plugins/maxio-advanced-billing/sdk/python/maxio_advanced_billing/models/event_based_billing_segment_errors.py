from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EventBasedBillingSegmentErrors(SdkBaseModel):
    errors: Optional[dict[str, Any]] = UNSET
    """The key of the object would be a number (an index in the request array) where the error occurred. In the value
    object, the key represents the field and the value is an array with error messages. In most cases, this object would
    contain just one key."""


class EventBasedBillingSegmentErrorsDict(TypedDict):
    errors: NotRequired[dict[str, Any]]
