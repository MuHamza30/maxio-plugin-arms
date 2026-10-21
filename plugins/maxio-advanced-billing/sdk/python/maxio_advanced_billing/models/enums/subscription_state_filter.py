from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionStateFilter(str, Enum):
    """Allowed values for filtering by the current state of the subscription."""

    ACTIVE = "active"
    CANCELED = "canceled"
    EXPIRED = "expired"
    EXPIRED_CARDS = "expired_cards"
    EXPIRED_CARDS_LIVE_SUBSCRIPTIONS = "expired_cards_(live_subscriptions)"
    EXPIRED_CARDS_ALL_SUBSCRIPTIONS = "expired_cards_(all_subscriptions)"
    ON_HOLD = "on_hold"
    AWAITING_SIGNUP = "awaiting_signup"
    AWAITING_SIGNUP_DATE = "awaiting_signup_date"
    PAST_DUE = "past_due"
    PENDING_CANCELLATION = "pending_cancellation"
    PENDING_RENEWAL = "pending_renewal"
    PREPAID_DUNNING = "prepaid_dunning"
    SUSPENDED = "suspended"
    TRIAL_ENDED = "trial_ended"
    TRIALING = "trialing"
    UNPAID = "unpaid"

    __str__ = str.__str__


SubscriptionStateFilterOrStr: TypeAlias = Annotated[
    SubscriptionStateFilter | str, open_enum_validator(SubscriptionStateFilter)
]
