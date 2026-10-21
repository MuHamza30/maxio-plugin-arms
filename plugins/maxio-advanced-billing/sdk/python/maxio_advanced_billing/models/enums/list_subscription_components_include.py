from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListSubscriptionComponentsInclude(str, Enum):
    SUBSCRIPTION = "subscription"
    HISTORIC_USAGES = "historic_usages"

    __str__ = str.__str__


ListSubscriptionComponentsIncludeOrStr: TypeAlias = Annotated[
    ListSubscriptionComponentsInclude | str, open_enum_validator(ListSubscriptionComponentsInclude)
]
