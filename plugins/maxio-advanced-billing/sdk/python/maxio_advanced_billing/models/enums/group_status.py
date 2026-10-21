from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GroupStatus(str, Enum):
    UNGROUPED = "ungrouped"
    GROUPED = "grouped"

    __str__ = str.__str__


GroupStatusOrStr: TypeAlias = Annotated[GroupStatus | str, open_enum_validator(GroupStatus)]
