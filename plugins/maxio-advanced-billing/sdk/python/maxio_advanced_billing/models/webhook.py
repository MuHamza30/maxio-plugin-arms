from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class Webhook(SdkBaseModel):
    event: Optional[str] = UNSET
    """A string describing which event type produced the given webhook"""

    id: Optional[int] = UNSET
    """The unique identifier for the webhook (unique across all of Chargify). This is not changed on a retry/replay of
    the same webhook, so it may be used to avoid duplicate action for the same event."""

    created_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when the webhook was created"""

    last_error: Optional[str] = UNSET
    """Text describing the status code and/or error from the last failed attempt to send the Webhook. When a webhook is
    retried and accepted, this field will be cleared."""

    last_error_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when the last non-acceptance occurred. If a webhook is later resent and accepted, this field
    will be cleared."""

    accepted_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp indicating when the webhook was accepted by the merchant endpoint. When a webhook is explicitly
    replayed by the merchant, this value will be cleared until it is accepted again."""

    last_sent_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when the most recent attempt was made to send the webhook"""

    last_sent_url: Optional[str] = UNSET
    """The url that the endpoint was last sent to."""

    successful: Optional[bool] = UNSET
    """“A boolean flag describing whether the webhook was accepted by the webhook endpoint for the most recent attempt.
    (Acceptance is defined by receiving a “200 OK” HTTP response within a reasonable timeframe, e.g., 15 seconds.)”"""

    body: Optional[str] = UNSET
    """The data sent within the webhook post"""

    signature: Optional[str] = UNSET
    """The calculated webhook signature"""

    signature_hmac_sha_256: Optional[str] = UNSET
    """The calculated HMAC-SHA-256 webhook signature"""


class WebhookDict(TypedDict):
    event: NotRequired[str]
    id: NotRequired[int]
    created_at: NotRequired[RFC3339DateTime]
    last_error: NotRequired[str]
    last_error_at: NotRequired[RFC3339DateTime]
    accepted_at: NotRequired[RFC3339DateTime | None]
    last_sent_at: NotRequired[RFC3339DateTime]
    last_sent_url: NotRequired[str]
    successful: NotRequired[bool]
    body: NotRequired[str]
    signature: NotRequired[str]
    signature_hmac_sha_256: NotRequired[str]
