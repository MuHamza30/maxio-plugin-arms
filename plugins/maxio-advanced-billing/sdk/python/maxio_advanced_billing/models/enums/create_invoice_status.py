from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreateInvoiceStatus(str, Enum):
    DRAFT = "draft"
    OPEN = "open"

    __str__ = str.__str__


CreateInvoiceStatusOrStr: TypeAlias = Annotated[CreateInvoiceStatus | str, open_enum_validator(CreateInvoiceStatus)]
