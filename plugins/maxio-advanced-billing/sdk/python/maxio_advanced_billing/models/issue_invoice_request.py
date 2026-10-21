from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.failed_payment_action import FailedPaymentAction, FailedPaymentActionOrStr


class IssueInvoiceRequest(SdkBaseModel):
    on_failed_payment: FailedPaymentActionOrStr = FailedPaymentAction.LEAVE_OPEN_INVOICE
    """Action taken when payment for an invoice fails:
    - ``leave_open_invoice`` - prepayments and credits applied to invoice; invoice status set to "open"; email sent to
        the customer for the issued invoice (if setting applies); payment failure recorded in the invoice history. This
        is the default option.
    - ``rollback_to_pending`` - prepayments and credits not applied; invoice remains in "pending" status; no email sent
        to the customer; payment failure recorded in the invoice history.
    - ``initiate_dunning`` - prepayments and credits applied to the invoice; invoice status set to "open"; email sent to
        the customer for the issued invoice (if setting applies); payment failure recorded in the invoice history;
        subscription will most likely go into "past_due" or "canceled" state (depending upon net terms and dunning
        settings)."""


class IssueInvoiceRequestDict(TypedDict):
    on_failed_payment: NotRequired[FailedPaymentActionOrStr]
