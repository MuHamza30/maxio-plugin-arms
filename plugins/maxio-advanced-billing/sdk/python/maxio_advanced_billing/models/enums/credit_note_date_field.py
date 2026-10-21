from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditNoteDateField(str, Enum):
    ISSUE_DATE = "issue_date"
    APPLIED_DATE = "applied_date"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"

    __str__ = str.__str__


CreditNoteDateFieldOrStr: TypeAlias = Annotated[CreditNoteDateField | str, open_enum_validator(CreditNoteDateField)]
