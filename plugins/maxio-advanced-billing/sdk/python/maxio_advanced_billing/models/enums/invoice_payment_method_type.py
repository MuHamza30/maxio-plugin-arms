from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoicePaymentMethodType(str, Enum):
    """The type of payment method used. Defaults to other."""

    CREDIT_CARD = "credit_card"
    CHECK = "check"
    CASH = "cash"
    MONEY_ORDER = "money_order"
    ACH = "ach"
    OTHER = "other"

    __str__ = str.__str__


InvoicePaymentMethodTypeOrStr: TypeAlias = Annotated[
    InvoicePaymentMethodType | str, open_enum_validator(InvoicePaymentMethodType)
]
