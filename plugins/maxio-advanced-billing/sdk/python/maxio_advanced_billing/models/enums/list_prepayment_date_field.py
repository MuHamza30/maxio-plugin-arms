from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListPrepaymentDateField(str, Enum):
    CREATED_AT = "created_at"
    APPLICATION_AT = "application_at"

    __str__ = str.__str__


ListPrepaymentDateFieldOrStr: TypeAlias = Annotated[
    ListPrepaymentDateField | str, open_enum_validator(ListPrepaymentDateField)
]
