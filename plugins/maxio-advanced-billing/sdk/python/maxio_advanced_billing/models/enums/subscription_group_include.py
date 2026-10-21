from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionGroupInclude(str, Enum):
    CURRENT_BILLING_AMOUNT_IN_CENTS = "current_billing_amount_in_cents"

    __str__ = str.__str__


SubscriptionGroupIncludeOrStr: TypeAlias = Annotated[
    SubscriptionGroupInclude | str, open_enum_validator(SubscriptionGroupInclude)
]
