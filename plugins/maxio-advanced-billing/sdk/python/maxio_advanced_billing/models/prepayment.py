from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.prepayment_method import PrepaymentMethodOrStr


class Prepayment(SdkBaseModel):
    id: int
    subscription_id: int
    amount_in_cents: int
    remaining_amount_in_cents: int
    refunded_amount_in_cents: Optional[int] = UNSET
    details: Optional[str] = UNSET
    external: bool
    memo: str
    payment_type: Optional[PrepaymentMethodOrStr] = UNSET
    """The payment type of the prepayment."""

    created_at: RFC3339DateTime


class PrepaymentDict(TypedDict):
    id: int
    subscription_id: int
    amount_in_cents: int
    remaining_amount_in_cents: int
    refunded_amount_in_cents: NotRequired[int]
    details: NotRequired[str]
    external: bool
    memo: str
    payment_type: NotRequired[PrepaymentMethodOrStr]
    created_at: RFC3339DateTime
