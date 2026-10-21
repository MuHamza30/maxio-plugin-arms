from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ChargifyEbb(SdkBaseModel):
    timestamp: Optional[RFC3339DateTime] = UNSET
    """This timestamp determines what billing period the event will be billed in. If your request payload does not
    include it, Chargify will add ``chargify.timestamp`` to the event payload and set the value to ``now``."""

    id: Optional[str] = UNSET
    """A unique ID set by Chargify. This field is reserved. If ``chargify.id`` is present in the request payload, it
    will be overwritten."""

    created_at: Optional[RFC3339DateTime] = UNSET
    """An ISO-8601 timestamp, set by Chargify at the time each event is recorded. This field is reserved. If
    ``chargify.created_at`` is present in the request payload, it will be overwritten."""

    uniqueness_token: Optional[str] = UNSET
    """User-defined string scoped per-stream. Duplicate events within a stream will be silently ignored. Tokens expire
    after 31 days."""

    subscription_id: Optional[int] = UNSET
    """Id of Maxio Advanced Billing Subscription which is connected to this event. Provide ``subscription_id`` if you
    configured ``chargify.subscription_id`` as Subscription Identifier in your Event Stream."""

    subscription_reference: Optional[str] = UNSET
    """Reference of Maxio Advanced Billing Subscription which is connected to this event. Provide
    ``subscription_reference`` if you configured ``chargify.subscription_reference`` as Subscription Identifier in your
    Event Stream."""


class ChargifyEbbDict(TypedDict):
    timestamp: NotRequired[RFC3339DateTime]
    id: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    uniqueness_token: NotRequired[str]
    subscription_id: NotRequired[int]
    subscription_reference: NotRequired[str]
