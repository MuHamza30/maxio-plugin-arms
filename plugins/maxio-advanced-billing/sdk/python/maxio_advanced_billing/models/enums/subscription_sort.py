from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionSort(str, Enum):
    SIGNUP_DATE = "signup_date"
    PERIOD_START = "period_start"
    PERIOD_END = "period_end"
    NEXT_ASSESSMENT = "next_assessment"
    UPDATED_AT = "updated_at"
    CREATED_AT = "created_at"
    TOTAL_PAYMENTS = "total_payments"
    ID = "id"
    OPEN_BALANCE = "open_balance"
    EXPIRES_AT = "expires_at"

    __str__ = str.__str__


SubscriptionSortOrStr: TypeAlias = Annotated[SubscriptionSort | str, open_enum_validator(SubscriptionSort)]
