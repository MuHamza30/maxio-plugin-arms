from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .credit_note import CreditNote, CreditNoteDict
from .enums.invoice_consolidation_level import InvoiceConsolidationLevelOrStr


class RefundInvoiceEventData(SdkBaseModel):
    """Example schema for an ``refund_invoice`` event"""

    apply_credit: bool
    """If true, credit was created and applied it to the invoice."""

    consolidation_level: Optional[InvoiceConsolidationLevelOrStr] = UNSET
    """Consolidation level of the invoice, which is applicable to invoice consolidation. It will hold one of the
    following values:

    * "none": A normal invoice with no consolidation.
    * "child": An invoice segment which has been combined into a consolidated invoice.
    * "parent": A consolidated invoice, whose contents are composed of invoice segments.

    "Parent" invoices do not have lines of their own, but they have subtotals and totals which aggregate the member
    invoice segments.

    See also the `invoice consolidation documentation
    <https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation>`__."""

    credit_note_attributes: CreditNote
    memo: Optional[str] = UNSET
    """The refund memo."""

    original_amount: Optional[str] = UNSET
    """The full, original amount of the refund."""

    payment_id: int
    """The ID of the payment transaction to be refunded."""

    refund_amount: str
    """The amount of the refund."""

    refund_id: int
    """The ID of the refund transaction."""

    transaction_time: RFC3339DateTime
    """The time the refund was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z"
    """


class RefundInvoiceEventDataDict(TypedDict):
    apply_credit: bool
    consolidation_level: NotRequired[InvoiceConsolidationLevelOrStr]
    credit_note_attributes: CreditNoteDict
    memo: NotRequired[str]
    original_amount: NotRequired[str]
    payment_id: int
    refund_amount: str
    refund_id: int
    transaction_time: RFC3339DateTime
