from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RefundInvoice(SdkBaseModel):
    """Refund an invoice or a segment of a consolidated invoice."""

    amount: str
    """The amount to be refunded in decimal format as a string. Example: "10.50". Must not exceed the remaining
    refundable balance of the payment."""

    memo: str
    """A description that will be attached to the refund"""

    payment_id: int
    """The ID of the payment to be refunded"""

    external: Optional[bool] = UNSET
    """Flag that marks refund as external (no money is returned to the customer). Defaults to ``false``."""

    apply_credit: Optional[bool] = UNSET
    """If set to true, creates credit and applies it to an invoice. Defaults to ``false``."""

    void_invoice: Optional[bool] = UNSET
    """If ``apply_credit`` is set to false and refunding full amount, if ``void_invoice`` is set to true, invoice will
    be voided after refund. Defaults to ``false``."""


class RefundInvoiceDict(TypedDict):
    amount: str
    memo: str
    payment_id: int
    external: NotRequired[bool]
    apply_credit: NotRequired[bool]
    void_invoice: NotRequired[bool]
