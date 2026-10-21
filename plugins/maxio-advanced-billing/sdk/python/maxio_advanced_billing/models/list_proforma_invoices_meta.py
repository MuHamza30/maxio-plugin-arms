from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListProformaInvoicesMeta(SdkBaseModel):
    total_count: Optional[int] = UNSET
    current_page: Optional[int] = UNSET
    total_pages: Optional[int] = UNSET
    status_code: Optional[int] = UNSET


class ListProformaInvoicesMetaDict(TypedDict):
    total_count: NotRequired[int]
    current_page: NotRequired[int]
    total_pages: NotRequired[int]
    status_code: NotRequired[int]
