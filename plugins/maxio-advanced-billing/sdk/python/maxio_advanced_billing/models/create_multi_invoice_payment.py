from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_invoice_payment_application import CreateInvoicePaymentApplication, CreateInvoicePaymentApplicationDict
from .enums.invoice_payment_method_type import InvoicePaymentMethodTypeOrStr
from .unions.amount1 import Amount1, Amount1Dict


class CreateMultiInvoicePayment(SdkBaseModel):
    memo: Optional[str] = UNSET
    """A description to be attached to the payment."""

    details: Optional[str] = UNSET
    """Additional information related to the payment method (eg. Check #)."""

    method: Optional[InvoicePaymentMethodTypeOrStr] = UNSET
    """The type of payment method used. Defaults to other."""

    amount: Amount1
    """Dollar amount of the sum of the invoices payment (eg. "10.50" => $10.50)."""

    received_on: Optional[str] = UNSET
    """Date reflecting when the payment was received from a customer. Must be in the past."""

    applications: list[CreateInvoicePaymentApplication]


class CreateMultiInvoicePaymentDict(TypedDict):
    memo: NotRequired[str]
    details: NotRequired[str]
    method: NotRequired[InvoicePaymentMethodTypeOrStr]
    amount: Amount1Dict
    received_on: NotRequired[str]
    applications: list[CreateInvoicePaymentApplicationDict]
