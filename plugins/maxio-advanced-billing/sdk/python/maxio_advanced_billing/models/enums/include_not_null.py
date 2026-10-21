from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludeNotNull(str, Enum):
    """Passed as a parameter to list methods to return only non null values."""

    NOT_NULL = "not_null"

    __str__ = str.__str__


IncludeNotNullOrStr: TypeAlias = Annotated[IncludeNotNull | str, open_enum_validator(IncludeNotNull)]
