from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListSubscriptionComponentsSort(str, Enum):
    ID = "id"
    UPDATED_AT = "updated_at"

    __str__ = str.__str__


ListSubscriptionComponentsSortOrStr: TypeAlias = Annotated[
    ListSubscriptionComponentsSort | str, open_enum_validator(ListSubscriptionComponentsSort)
]
