from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SendInvoiceRequest(SdkBaseModel):
    recipient_emails: Optional[list[str]] = UNSET
    cc_recipient_emails: Optional[list[str]] = UNSET
    bcc_recipient_emails: Optional[list[str]] = UNSET
    attachment_urls: Optional[list[str]] = UNSET
    """Array of URLs to files to attach to the invoice email. Max 10 files, 10MB each."""


class SendInvoiceRequestDict(TypedDict):
    recipient_emails: NotRequired[list[str]]
    cc_recipient_emails: NotRequired[list[str]]
    bcc_recipient_emails: NotRequired[list[str]]
    attachment_urls: NotRequired[list[str]]
