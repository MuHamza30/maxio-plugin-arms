from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LineItemTransactionType(str, Enum):
    """A handle for the line item transaction type"""

    CHARGE = "charge"
    CREDIT = "credit"
    ADJUSTMENT = "adjustment"
    PAYMENT = "payment"
    REFUND = "refund"
    INFO_TRANSACTION = "info_transaction"
    PAYMENT_AUTHORIZATION = "payment_authorization"

    __str__ = str.__str__


LineItemTransactionTypeOrStr: TypeAlias = Annotated[
    LineItemTransactionType | str, open_enum_validator(LineItemTransactionType)
]
