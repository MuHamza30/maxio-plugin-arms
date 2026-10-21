from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncludeOption(str, Enum):
    _0 = "0"
    _1 = "1"

    __str__ = str.__str__


IncludeOptionOrStr: TypeAlias = Annotated[IncludeOption | str, open_enum_validator(IncludeOption)]
