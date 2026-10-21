from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionPurgeType(str, Enum):
    CUSTOMER = "customer"
    PAYMENT_PROFILE = "payment_profile"

    __str__ = str.__str__


SubscriptionPurgeTypeOrStr: TypeAlias = Annotated[
    SubscriptionPurgeType | str, open_enum_validator(SubscriptionPurgeType)
]
