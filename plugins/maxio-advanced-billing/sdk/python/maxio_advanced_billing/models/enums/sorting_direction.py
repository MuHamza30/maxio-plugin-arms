from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SortingDirection(str, Enum):
    """Used for sorting results."""

    ASC = "asc"
    DESC = "desc"

    __str__ = str.__str__


SortingDirectionOrStr: TypeAlias = Annotated[SortingDirection | str, open_enum_validator(SortingDirection)]
