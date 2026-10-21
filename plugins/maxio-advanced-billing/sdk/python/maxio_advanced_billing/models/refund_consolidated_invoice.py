from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.segment_uids import SegmentUids, SegmentUidsDict


class RefundConsolidatedInvoice(SdkBaseModel):
    """Refund consolidated invoice."""

    memo: str
    """A description for the refund"""

    payment_id: int
    """The ID of the payment to be refunded"""

    segment_uids: SegmentUids
    """An array of segment uids to refund or the string 'all' to indicate that all segments should be refunded"""

    external: Optional[bool] = UNSET
    """Flag that marks refund as external (no money is returned to the customer). Defaults to ``false``."""

    apply_credit: Optional[bool] = UNSET
    """If set to true, creates credit and applies it to an invoice. Defaults to ``false``."""

    amount: Optional[str] = UNSET
    """The amount of payment to be refunded in decimal format. Example: "10.50". This will default to the full amount of
    the payment if not provided."""


class RefundConsolidatedInvoiceDict(TypedDict):
    memo: str
    payment_id: int
    segment_uids: SegmentUidsDict
    external: NotRequired[bool]
    apply_credit: NotRequired[bool]
    amount: NotRequired[str]
