from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IssueAdvanceInvoiceRequest(SdkBaseModel):
    force: Optional[bool] = UNSET


class IssueAdvanceInvoiceRequestDict(TypedDict):
    force: NotRequired[bool]
