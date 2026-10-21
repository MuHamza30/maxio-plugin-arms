from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_subscription import WebhookSubscriptionOrStr


class CreateOrUpdateEndpoint(SdkBaseModel):
    """Used to Create or Update Endpoint."""

    url: str
    webhook_subscriptions: list[WebhookSubscriptionOrStr]


class CreateOrUpdateEndpointDict(TypedDict):
    url: str
    webhook_subscriptions: list[WebhookSubscriptionOrStr]
