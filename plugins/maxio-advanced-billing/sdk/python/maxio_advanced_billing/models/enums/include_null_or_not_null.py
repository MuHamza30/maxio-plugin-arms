from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludeNullOrNotNull(str, Enum):
    """Allows to filter by ``not_null`` or ``null``."""

    NOT_NULL = "not_null"
    NULL = "null"

    __str__ = str.__str__


IncludeNullOrNotNullOrStr: TypeAlias = Annotated[IncludeNullOrNotNull | str, open_enum_validator(IncludeNullOrNotNull)]
