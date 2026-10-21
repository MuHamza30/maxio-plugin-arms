from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionGroupsListInclude(str, Enum):
    ACCOUNT_BALANCES = "account_balances"

    __str__ = str.__str__


SubscriptionGroupsListIncludeOrStr: TypeAlias = Annotated[
    SubscriptionGroupsListInclude | str, open_enum_validator(SubscriptionGroupsListInclude)
]
