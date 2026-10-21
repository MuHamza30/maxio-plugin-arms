from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionListInclude(str, Enum):
    SELF_SERVICE_PAGE_TOKEN = "self_service_page_token"
    CURRENT_ACCOUNT_BALANCE_IN_CENTS = "current_account_balance_in_cents"
    CURRENT_BILLING_AMOUNT = "current_billing_amount"
    COUPONS = "coupons"

    __str__ = str.__str__


SubscriptionListIncludeOrStr: TypeAlias = Annotated[
    SubscriptionListInclude | str, open_enum_validator(SubscriptionListInclude)
]
