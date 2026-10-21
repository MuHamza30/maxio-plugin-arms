from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListSubscriptionComponentsFilter(SdkBaseModel):
    currencies: Optional[list[str]] = UNSET
    """Allows fetching components allocation with matching currency based on provided values. Use in query
    ``filter[currencies]=EUR,USD``."""

    use_site_exchange_rate: Optional[bool] = UNSET
    """Allows fetching components allocation with matching use_site_exchange_rate based on provided value. Use in query
    ``filter[use_site_exchange_rate]=true``."""


class ListSubscriptionComponentsFilterDict(TypedDict):
    currencies: NotRequired[list[str]]
    use_site_exchange_rate: NotRequired[bool]
