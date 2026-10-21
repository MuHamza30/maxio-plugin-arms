from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GroupType(str, Enum):
    SINGLE_CUSTOMER = "single_customer"
    MULTIPLE_CUSTOMERS = "multiple_customers"

    __str__ = str.__str__


GroupTypeOrStr: TypeAlias = Annotated[GroupType | str, open_enum_validator(GroupType)]
