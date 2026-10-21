from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SortBy(str, Enum):
    NAME = "name"
    UPDATED_AT = "updated_at"
    KIND = "kind"
    VALUE_TYPE = "value_type"

    __str__ = str.__str__


SortByOrStr: TypeAlias = Annotated[SortBy | str, open_enum_validator(SortBy)]
