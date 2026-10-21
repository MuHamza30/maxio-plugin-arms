from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrepaymentMethod(str, Enum):
    CHECK = "check"
    CASH = "cash"
    MONEY_ORDER = "money_order"
    ACH = "ach"
    PAYPAL_ACCOUNT = "paypal_account"
    CREDIT_CARD = "credit_card"
    OTHER = "other"

    __str__ = str.__str__


PrepaymentMethodOrStr: TypeAlias = Annotated[PrepaymentMethod | str, open_enum_validator(PrepaymentMethod)]
