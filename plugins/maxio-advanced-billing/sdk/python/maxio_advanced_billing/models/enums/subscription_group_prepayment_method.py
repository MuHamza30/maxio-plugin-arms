from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionGroupPrepaymentMethod(str, Enum):
    CHECK = "check"
    CASH = "cash"
    MONEY_ORDER = "money_order"
    ACH = "ach"
    PAYPAL_ACCOUNT = "paypal_account"
    OTHER = "other"

    __str__ = str.__str__


SubscriptionGroupPrepaymentMethodOrStr: TypeAlias = Annotated[
    SubscriptionGroupPrepaymentMethod | str, open_enum_validator(SubscriptionGroupPrepaymentMethod)
]
