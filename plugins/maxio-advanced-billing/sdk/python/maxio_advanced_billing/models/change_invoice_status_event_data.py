from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.invoice_consolidation_level import InvoiceConsolidationLevelOrStr
from .enums.invoice_status import InvoiceStatusOrStr


class ChangeInvoiceStatusEventData(SdkBaseModel):
    """Example schema for an ``change_invoice_status`` event"""

    gateway_trans_id: Optional[str] = UNSET
    """Identifier for the transaction within the payment gateway."""

    amount: Optional[str] = UNSET
    """The monetary value associated with the linked payment, expressed in dollars."""

    from_status: InvoiceStatusOrStr
    """The status of the invoice before any changes occurred. See `Invoice Statuses
    <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses>`__
    for more."""

    to_status: InvoiceStatusOrStr
    """The updated status of the invoice after changes have been made. See `Invoice Statuses
    <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses>`__
    for more."""

    consolidation_level: Optional[InvoiceConsolidationLevelOrStr] = UNSET


class ChangeInvoiceStatusEventDataDict(TypedDict):
    gateway_trans_id: NotRequired[str]
    amount: NotRequired[str]
    from_status: InvoiceStatusOrStr
    to_status: InvoiceStatusOrStr
    consolidation_level: NotRequired[InvoiceConsolidationLevelOrStr]
