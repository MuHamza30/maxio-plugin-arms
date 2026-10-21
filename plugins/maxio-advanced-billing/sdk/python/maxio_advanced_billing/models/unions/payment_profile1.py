from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..apple_pay_payment_profile import ApplePayPaymentProfile, ApplePayPaymentProfileDict
from ..bank_account_payment_profile import BankAccountPaymentProfile, BankAccountPaymentProfileDict
from ..credit_card_payment_profile import CreditCardPaymentProfile, CreditCardPaymentProfileDict
from ..paypal_payment_profile import PaypalPaymentProfile, PaypalPaymentProfileDict

PaymentProfile1: TypeAlias = Annotated[
    (
        Annotated[ApplePayPaymentProfile, Tag("apple_pay")]
        | Annotated[BankAccountPaymentProfile, Tag("bank_account")]
        | Annotated[CreditCardPaymentProfile, Tag("credit_card")]
        | Annotated[PaypalPaymentProfile, Tag("paypal_account")]
    ),
    WireDiscriminator("payment_type"),
]

PaymentProfile1Dict: TypeAlias = (
    ApplePayPaymentProfileDict | BankAccountPaymentProfileDict | CreditCardPaymentProfileDict | PaypalPaymentProfileDict
)
