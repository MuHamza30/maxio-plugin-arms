from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProformaInvoiceStatus(str, Enum):
    DRAFT = "draft"
    VOIDED = "voided"
    ARCHIVED = "archived"

    __str__ = str.__str__


ProformaInvoiceStatusOrStr: TypeAlias = Annotated[
    ProformaInvoiceStatus | str, open_enum_validator(ProformaInvoiceStatus)
]
