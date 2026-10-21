from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.list_prepayment_date_field import ListPrepaymentDateFieldOrStr


class ListPrepaymentsFilter(SdkBaseModel):
    date_field: Optional[ListPrepaymentDateFieldOrStr] = UNSET
    """The type of filter you would like to apply to your search. ``created_at`` - Time when prepayment was created.
    ``application_at`` - Time when prepayment was applied to invoice. Use in query ``filter[date_field]=created_at``."""

    start_date: Optional[Date] = UNSET
    """The start date (format YYYY-MM-DD) with which to filter the date_field. Returns prepayments with a timestamp at
    or after midnight (12:00:00 AM) in your site's time zone on the date specified. Use in query:
    ``filter[start_date]=2011-12-15``."""

    end_date: Optional[Date] = UNSET
    """The end date (format YYYY-MM-DD) with which to filter the date_field. Returns prepayments with a timestamp up to
    and including 11:59:59PM in your site's time zone on the date specified. Use in query:
    ``filter[end_date]=2011-12-15``."""


class ListPrepaymentsFilterDict(TypedDict):
    date_field: NotRequired[ListPrepaymentDateFieldOrStr]
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
