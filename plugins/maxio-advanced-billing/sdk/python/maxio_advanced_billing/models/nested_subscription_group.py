from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NestedSubscriptionGroup(SdkBaseModel):
    uid: Optional[str] = UNSET
    """The UID for the group"""

    scheme: Optional[int] = UNSET
    """Whether the group is configured to rely on a primary subscription for billing. At this time, it will always be
    1."""

    primary_subscription_id: Optional[int] = UNSET
    """The subscription ID of the primary within the group. Applicable to scheme 1."""

    primary: Optional[bool] = UNSET
    """A boolean indicating whether the subscription is the primary in the group. Applicable to scheme 1."""


class NestedSubscriptionGroupDict(TypedDict):
    uid: NotRequired[str]
    scheme: NotRequired[int]
    primary_subscription_id: NotRequired[int]
    primary: NotRequired[bool]
