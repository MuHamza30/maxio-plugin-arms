from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentType(str, Enum):
    CREDIT_CARD = "credit_card"
    BANK_ACCOUNT = "bank_account"
    PAYPAL_ACCOUNT = "paypal_account"
    APPLE_PAY = "apple_pay"

    __str__ = str.__str__


PaymentTypeOrStr: TypeAlias = Annotated[PaymentType | str, open_enum_validator(PaymentType)]
