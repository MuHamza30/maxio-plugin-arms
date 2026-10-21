from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoicePaymentApplication(SdkBaseModel):
    invoice_uid: Optional[str] = UNSET
    """Unique identifier for the paid invoice. It has the prefix "inv_" followed by alphanumeric characters."""

    application_uid: Optional[str] = UNSET
    """Unique identifier for the payment. It has the prefix "pmt_" followed by alphanumeric characters."""

    applied_amount: Optional[str] = UNSET
    """Dollar amount of the paid invoice."""


class InvoicePaymentApplicationDict(TypedDict):
    invoice_uid: NotRequired[str]
    application_uid: NotRequired[str]
    applied_amount: NotRequired[str]
