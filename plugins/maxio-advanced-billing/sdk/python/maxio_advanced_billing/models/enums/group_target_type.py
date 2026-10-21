from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GroupTargetType(str, Enum):
    """The type of object indicated by the id attribute."""

    CUSTOMER = "customer"
    SUBSCRIPTION = "subscription"
    SELF = "self"
    PARENT = "parent"
    ELDEST = "eldest"

    __str__ = str.__str__


GroupTargetTypeOrStr: TypeAlias = Annotated[GroupTargetType | str, open_enum_validator(GroupTargetType)]
