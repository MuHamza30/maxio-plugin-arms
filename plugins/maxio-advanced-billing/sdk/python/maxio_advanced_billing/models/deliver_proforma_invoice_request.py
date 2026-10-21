from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeliverProformaInvoiceRequest(SdkBaseModel):
    recipient_emails: Optional[list[str]] = UNSET
    cc_recipient_emails: Optional[list[str]] = UNSET
    bcc_recipient_emails: Optional[list[str]] = UNSET


class DeliverProformaInvoiceRequestDict(TypedDict):
    recipient_emails: NotRequired[list[str]]
    cc_recipient_emails: NotRequired[list[str]]
    bcc_recipient_emails: NotRequired[list[str]]
