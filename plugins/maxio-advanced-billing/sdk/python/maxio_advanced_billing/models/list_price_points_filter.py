from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, RFC3339DateTime, SdkBaseModel
from .enums.basic_date_field import BasicDateFieldOrStr
from .enums.include_null_or_not_null import IncludeNullOrNotNullOrStr
from .enums.price_point_type import PricePointTypeOrStr


class ListPricePointsFilter(SdkBaseModel):
    date_field: Optional[BasicDateFieldOrStr] = UNSET
    """The type of filter you would like to apply to your search. Use in query: ``filter[date_field]=created_at``."""

    start_date: Optional[Date] = UNSET
    """The start date (format YYYY-MM-DD) with which to filter the date_field. Returns price points with a timestamp at
    or after midnight (12:00:00 AM) in your site’s time zone on the date specified."""

    end_date: Optional[Date] = UNSET
    """The end date (format YYYY-MM-DD) with which to filter the date_field. Returns price points with a timestamp up to
    and including 11:59:59PM in your site’s time zone on the date specified."""

    start_datetime: Optional[RFC3339DateTime] = UNSET
    """The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns price points
    with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's
    time zone will be used. If provided, this parameter will be used instead of start_date."""

    end_datetime: Optional[RFC3339DateTime] = UNSET
    """The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns price points with
    a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's
    time zone will be used. If provided, this parameter will be used instead of end_date."""

    type_: Optional[list[PricePointTypeOrStr]] = Field(default=UNSET, alias="type")
    """Allows fetching price points with matching type. Use in query: ``filter[type]=custom,catalog``."""

    ids: Optional[list[int]] = UNSET
    """Allows fetching price points with matching id based on provided values. Use in query: ``filter[ids]=1,2,3``."""

    archived_at: Optional[IncludeNullOrNotNullOrStr] = UNSET
    """Allows fetching price points only if archived_at is present or not. Use in query:
    ``filter[archived_at]=not_null``."""


class ListPricePointsFilterDict(TypedDict):
    date_field: NotRequired[BasicDateFieldOrStr]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
    start_datetime: NotRequired[RFC3339DateTime]
    end_datetime: NotRequired[RFC3339DateTime]
    type_: NotRequired[list[PricePointTypeOrStr]]
    ids: NotRequired[list[int]]
    archived_at: NotRequired[IncludeNullOrNotNullOrStr]
