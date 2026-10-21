from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FirstChargeType(str, Enum):
    PRORATED = "prorated"
    IMMEDIATE = "immediate"
    DELAYED = "delayed"

    __str__ = str.__str__


FirstChargeTypeOrStr: TypeAlias = Annotated[FirstChargeType | str, open_enum_validator(FirstChargeType)]
