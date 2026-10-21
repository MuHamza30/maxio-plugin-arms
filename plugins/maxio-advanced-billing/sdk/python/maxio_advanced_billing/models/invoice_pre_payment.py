from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoicePrePayment(SdkBaseModel):
    subscription_id: Optional[int] = UNSET
    """The subscription id for the prepayment account"""

    amount_in_cents: Optional[int] = UNSET
    """The amount in cents of the prepayment that was created as a result of this payment."""

    ending_balance_in_cents: Optional[int] = UNSET
    """The total balance of the prepayment account for this subscription including any prior prepayments"""


class InvoicePrePaymentDict(TypedDict):
    subscription_id: NotRequired[int]
    amount_in_cents: NotRequired[int]
    ending_balance_in_cents: NotRequired[int]
