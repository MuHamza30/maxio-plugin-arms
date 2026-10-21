from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EntitlementPeriodicityUnit(str, Enum):
    """The recurring window over which a ``usage_limit`` feature's allowance resets."""

    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    __str__ = str.__str__


EntitlementPeriodicityUnitOrStr: TypeAlias = Annotated[
    EntitlementPeriodicityUnit | str, open_enum_validator(EntitlementPeriodicityUnit)
]
