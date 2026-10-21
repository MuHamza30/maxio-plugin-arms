from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceDateField(str, Enum):
    CREATED_AT = "created_at"
    DUE_DATE = "due_date"
    ISSUE_DATE = "issue_date"
    UPDATED_AT = "updated_at"
    PAID_DATE = "paid_date"

    __str__ = str.__str__


InvoiceDateFieldOrStr: TypeAlias = Annotated[InvoiceDateField | str, open_enum_validator(InvoiceDateField)]
