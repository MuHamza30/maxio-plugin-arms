from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreatePrepaymentMethod(str, Enum):
    """When the ``method`` specified is ``"credit_card_on_file"``, the prepayment amount will be collected using the
    default credit card payment profile and applied to the prepayment account balance. This is especially useful for
    manual replenishment of prepaid subscriptions."""

    CHECK = "check"
    CASH = "cash"
    MONEY_ORDER = "money_order"
    ACH = "ach"
    PAYPAL_ACCOUNT = "paypal_account"
    CREDIT_CARD = "credit_card"
    CREDIT_CARD_ON_FILE = "credit_card_on_file"
    OTHER = "other"

    __str__ = str.__str__


CreatePrepaymentMethodOrStr: TypeAlias = Annotated[
    CreatePrepaymentMethod | str, open_enum_validator(CreatePrepaymentMethod)
]
