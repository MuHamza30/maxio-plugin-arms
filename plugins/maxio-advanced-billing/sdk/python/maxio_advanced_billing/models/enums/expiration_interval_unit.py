from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExpirationIntervalUnit(str, Enum):
    DAY = "day"
    MONTH = "month"
    NEVER = "never"

    __str__ = str.__str__


ExpirationIntervalUnitOrStr: TypeAlias = Annotated[
    ExpirationIntervalUnit | str, open_enum_validator(ExpirationIntervalUnit)
]
