from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.invoice_payment_method_type import InvoicePaymentMethodTypeOrStr
from .unions.amount import Amount, AmountDict


class CreateInvoicePayment(SdkBaseModel):
    amount: Optional[Amount] = UNSET
    """A string of the dollar amount to be refunded (eg. "10.50" => $10.50)"""

    memo: Optional[str] = UNSET
    """A description to be attached to the payment. Applicable only to ``external`` payments."""

    method: Optional[InvoicePaymentMethodTypeOrStr] = UNSET
    """The type of payment method used. Defaults to other."""

    details: Optional[str] = UNSET
    """Additional information related to the payment method (eg. Check #). Applicable only to ``external`` payments."""

    payment_profile_id: Optional[int] = UNSET
    """The ID of the payment profile to be used for the payment."""

    received_on: Optional[Date] = UNSET
    """Date reflecting when the payment was received from a customer. Must be in the past. Applicable only to
    ``external`` payments."""


class CreateInvoicePaymentDict(TypedDict):
    amount: NotRequired[AmountDict]
    memo: NotRequired[str]
    method: NotRequired[InvoicePaymentMethodTypeOrStr]
    details: NotRequired[str]
    payment_profile_id: NotRequired[int]
    received_on: NotRequired[Date]
