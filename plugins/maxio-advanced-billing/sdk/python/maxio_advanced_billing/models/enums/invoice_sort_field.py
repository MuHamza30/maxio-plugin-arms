from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceSortField(str, Enum):
    STATUS = "status"
    TOTAL_AMOUNT = "total_amount"
    DUE_AMOUNT = "due_amount"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    ISSUE_DATE = "issue_date"
    DUE_DATE = "due_date"
    NUMBER = "number"

    __str__ = str.__str__


InvoiceSortFieldOrStr: TypeAlias = Annotated[InvoiceSortField | str, open_enum_validator(InvoiceSortField)]
