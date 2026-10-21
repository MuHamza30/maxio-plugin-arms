from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Kind1(str, Enum):
    """Determines the direction of the movement. The amount itself is always sent positive."""

    GRANT = "grant"
    DEBIT = "debit"

    __str__ = str.__str__


Kind1OrStr: TypeAlias = Annotated[Kind1 | str, open_enum_validator(Kind1)]
