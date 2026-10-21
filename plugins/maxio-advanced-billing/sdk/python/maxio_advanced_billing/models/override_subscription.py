from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class OverrideSubscription(SdkBaseModel):
    activated_at: Optional[RFC3339DateTime] = UNSET
    """Can be used to record an external signup date. Chargify uses this field to record when a subscription first goes
    active (either at signup or at trial end). Only ISO8601 format is supported."""

    canceled_at: Optional[RFC3339DateTime] = UNSET
    """Can be used to record an external cancellation date. Chargify sets this field automatically when a subscription
    is canceled, whether by request or via dunning. Only ISO8601 format is supported."""

    cancellation_message: Optional[str] = UNSET
    """Can be used to record a reason for the original cancellation."""

    expires_at: Optional[RFC3339DateTime] = UNSET
    """Can be used to record an external expiration date. Chargify sets this field automatically when a subscription
    expires (ceases billing) after a prescribed amount of time. Only ISO8601 format is supported. This field is not
    supported when Multi-frequency is enabled for the Site. To change the Term End of a Subscription, use the Update
    Subscription endpoint."""

    current_period_starts_at: Optional[RFC3339DateTime] = UNSET
    """Can only be used when a subscription is unbilled, which happens when a future initial billing date is passed at
    subscription creation. The value passed must be before the current date and time. Allows you to set when the period
    started so mid period component allocations have the correct proration. Only ISO8601 format is supported."""


class OverrideSubscriptionDict(TypedDict):
    activated_at: NotRequired[RFC3339DateTime]
    canceled_at: NotRequired[RFC3339DateTime]
    cancellation_message: NotRequired[str]
    expires_at: NotRequired[RFC3339DateTime]
    current_period_starts_at: NotRequired[RFC3339DateTime]
