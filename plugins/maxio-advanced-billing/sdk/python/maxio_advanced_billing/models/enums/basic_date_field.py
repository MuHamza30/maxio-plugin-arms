from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BasicDateField(str, Enum):
    """Allows to filter by ``created_at`` or ``updated_at``."""

    UPDATED_AT = "updated_at"
    CREATED_AT = "created_at"

    __str__ = str.__str__


BasicDateFieldOrStr: TypeAlias = Annotated[BasicDateField | str, open_enum_validator(BasicDateField)]
