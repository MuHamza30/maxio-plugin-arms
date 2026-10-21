from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, RFC3339DateTime, SdkBaseModel
from .enums.basic_date_field import BasicDateFieldOrStr


class ListCouponsFilter(SdkBaseModel):
    date_field: Optional[BasicDateFieldOrStr] = UNSET
    """The type of filter you would like to apply to your search. Use in query ``filter[date_field]=created_at``."""

    start_date: Optional[Date] = UNSET
    """The start date (format YYYY-MM-DD) with which to filter the date_field. Returns coupons with a timestamp at or
    after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use in query
    ``filter[start_date]=2011-12-17``."""

    end_date: Optional[Date] = UNSET
    """The end date (format YYYY-MM-DD) with which to filter the date_field. Returns coupons with a timestamp up to and
    including 11:59:59PM in your site’s time zone on the date specified. Use in query
    ``filter[end_date]=2011-12-15``."""

    start_datetime: Optional[RFC3339DateTime] = UNSET
    """The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns coupons with a
    timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time
    zone will be used. If provided, this parameter will be used instead of start_date. Use in query
    ``filter[start_datetime]=2011-12-19T10:15:30+01:00``."""

    end_datetime: Optional[RFC3339DateTime] = UNSET
    """The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns coupons with a
    timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time
    zone will be used. If provided, this parameter will be used instead of end_date. Use in query
    ``filter[end_datetime]=2011-12-1T10:15:30+01:00``."""

    ids: Optional[list[int]] = UNSET
    """Allows fetching coupons with matching id based on provided values. Use in query ``filter[ids]=1,2,3``."""

    codes: Optional[list[str]] = UNSET
    """Allows fetching coupons with matching codes based on provided values. Use in query
    ``filter[codes]=free,free_trial``."""

    use_site_exchange_rate: Optional[bool] = UNSET
    """If true, restricts the list to coupons whose pricing is recalculated from the site’s current exchange rates, so
    their currency_prices array contains on-the-fly conversions rather than stored price records. If false, restricts
    the list to coupons that have manually defined amounts for each currency, ensuring the response includes the saved
    currency_prices entries instead of exchange-rate-derived values. Use in query
    ``filter[use_site_exchange_rate]=true``."""

    include_archived: Optional[bool] = UNSET
    """Controls returning archived coupons."""


class ListCouponsFilterDict(TypedDict):
    date_field: NotRequired[BasicDateFieldOrStr]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    start_datetime: NotRequired[RFC3339DateTime]
    end_datetime: NotRequired[RFC3339DateTime]
    ids: NotRequired[list[int]]
    codes: NotRequired[list[str]]
    use_site_exchange_rate: NotRequired[bool]
    include_archived: NotRequired[bool]
