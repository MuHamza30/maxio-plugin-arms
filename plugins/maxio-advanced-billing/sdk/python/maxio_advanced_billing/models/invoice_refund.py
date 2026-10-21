from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class InvoiceRefund(SdkBaseModel):
    transaction_id: Optional[int] = UNSET
    payment_id: Optional[int] = UNSET
    memo: Optional[str] = UNSET
    original_amount: Optional[str] = UNSET
    applied_amount: Optional[str] = UNSET
    gateway_transaction_id: OptionalNullable[str] = UNSET
    """The transaction ID for the refund as returned from the payment gateway"""

    gateway_used: Optional[str] = UNSET
    gateway_handle: OptionalNullable[str] = UNSET
    ach_late_reject: OptionalNullable[bool] = UNSET


class InvoiceRefundDict(TypedDict):
    transaction_id: NotRequired[int]
    payment_id: NotRequired[int]
    memo: NotRequired[str]
    original_amount: NotRequired[str]
    applied_amount: NotRequired[str]
    gateway_transaction_id: NotRequired[str | None]
    gateway_used: NotRequired[str]
    gateway_handle: NotRequired[str | None]
    ach_late_reject: NotRequired[bool | None]
