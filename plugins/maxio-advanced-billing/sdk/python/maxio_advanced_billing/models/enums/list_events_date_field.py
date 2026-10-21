from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListEventsDateField(str, Enum):
    CREATED_AT = "created_at"

    __str__ = str.__str__


ListEventsDateFieldOrStr: TypeAlias = Annotated[ListEventsDateField | str, open_enum_validator(ListEventsDateField)]
