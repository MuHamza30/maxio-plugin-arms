from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, RFC3339DateTime, SdkBaseModel
from .enums.subscription_list_date_field import SubscriptionListDateFieldOrStr
from .enums.subscription_state_filter import SubscriptionStateFilterOrStr


class SubscriptionFilter(SdkBaseModel):
    """Nested filter used for List Subscription Components For Site Filter"""

    states: Optional[list[SubscriptionStateFilterOrStr]] = UNSET
    """Allows fetching components allocations that belong to the subscription with matching states based on provided
    values. To use this filter you also have to include the following param in the request ``include=subscription``. Use
    in query ``filter[subscription][states]=active,canceled&include=subscription``."""

    date_field: Optional[SubscriptionListDateFieldOrStr] = UNSET
    """The type of filter you'd like to apply to your search. To use this filter you also have to include the following
    param in the request ``include=subscription``."""

    start_date: Optional[Date] = UNSET
    """The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components that belong to the
    subscription with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. To
    use this filter you also have to include the following param in the request ``include=subscription``."""

    end_date: Optional[Date] = UNSET
    """The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components that belong to the
    subscription with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. To use
    this filter you also have to include the following param in the request ``include=subscription``."""

    start_datetime: Optional[RFC3339DateTime] = UNSET
    """The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components that
    belong to the subscription with a timestamp at or after exact time provided in query. You can specify timezone in
    query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead of
    start_date. To use this filter you also have to include the following param in the request
    ``include=subscription``."""

    end_datetime: Optional[RFC3339DateTime] = UNSET
    """The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components that
    belong to the subscription with a timestamp at or before exact time provided in query. You can specify timezone in
    query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead of end_date.
    To use this filter you also have to include the following param in the request ``include=subscription``."""


class SubscriptionFilterDict(TypedDict):
    states: NotRequired[list[SubscriptionStateFilterOrStr]]
    date_field: NotRequired[SubscriptionListDateFieldOrStr]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    start_datetime: NotRequired[RFC3339DateTime]
    end_datetime: NotRequired[RFC3339DateTime]
