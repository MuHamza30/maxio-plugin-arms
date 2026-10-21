from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription_filter import SubscriptionFilter, SubscriptionFilterDict


class ListSubscriptionComponentsForSiteFilter(SdkBaseModel):
    currencies: Optional[list[str]] = UNSET
    """Allows fetching components allocation with matching currency based on provided values. Use in query
    ``filter[currencies]=USD,EUR``."""

    use_site_exchange_rate: Optional[bool] = UNSET
    """Allows fetching components allocation with matching use_site_exchange_rate based on provided value. Use in query
    ``filter[use_site_exchange_rate]=true``."""

    subscription: Optional[SubscriptionFilter] = UNSET
    """Nested filter used for List Subscription Components For Site Filter"""


class ListSubscriptionComponentsForSiteFilterDict(TypedDict):
    currencies: NotRequired[list[str]]
    use_site_exchange_rate: NotRequired[bool]
    subscription: NotRequired[SubscriptionFilterDict]
