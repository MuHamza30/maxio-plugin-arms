from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..payment_method_apple_pay import PaymentMethodApplePay, PaymentMethodApplePayDict
from ..payment_method_bank_account import PaymentMethodBankAccount, PaymentMethodBankAccountDict
from ..payment_method_credit_card import PaymentMethodCreditCard, PaymentMethodCreditCardDict
from ..payment_method_external import PaymentMethodExternal, PaymentMethodExternalDict
from ..payment_method_paypal import PaymentMethodPaypal, PaymentMethodPaypalDict

InvoiceEventPayment: TypeAlias = Annotated[
    (
        Annotated[PaymentMethodApplePay, Tag("apple_pay")]
        | Annotated[PaymentMethodBankAccount, Tag("bank_account")]
        | Annotated[PaymentMethodCreditCard, Tag("credit_card")]
        | Annotated[PaymentMethodExternal, Tag("external")]
        | Annotated[PaymentMethodPaypal, Tag("paypal_account")]
    ),
    WireDiscriminator("type"),
]
"""A nested data structure detailing the method of payment"""

InvoiceEventPaymentDict: TypeAlias = (
    PaymentMethodApplePayDict
    | PaymentMethodBankAccountDict
    | PaymentMethodCreditCardDict
    | PaymentMethodExternalDict
    | PaymentMethodPaypalDict
)
