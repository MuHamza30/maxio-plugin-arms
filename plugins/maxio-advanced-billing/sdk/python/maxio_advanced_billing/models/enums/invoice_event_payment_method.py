from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceEventPaymentMethod(str, Enum):
    APPLE_PAY = "apple_pay"
    BANK_ACCOUNT = "bank_account"
    CREDIT_CARD = "credit_card"
    EXTERNAL = "external"
    PAYPAL_ACCOUNT = "paypal_account"

    __str__ = str.__str__


InvoiceEventPaymentMethodOrStr: TypeAlias = Annotated[
    InvoiceEventPaymentMethod | str, open_enum_validator(InvoiceEventPaymentMethod)
]
