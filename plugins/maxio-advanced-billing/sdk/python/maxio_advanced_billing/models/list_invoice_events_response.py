from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.invoice_event import InvoiceEvent, InvoiceEventDict


class ListInvoiceEventsResponse(SdkBaseModel):
    events: Optional[list[InvoiceEvent]] = UNSET
    page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    total_pages: Optional[int] = UNSET


class ListInvoiceEventsResponseDict(TypedDict):
    events: NotRequired[list[InvoiceEventDict]]
    page: NotRequired[int]
    per_page: NotRequired[int]
    total_pages: NotRequired[int]
