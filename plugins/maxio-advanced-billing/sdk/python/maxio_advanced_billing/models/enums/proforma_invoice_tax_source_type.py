from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProformaInvoiceTaxSourceType(str, Enum):
    TAX = "Tax"
    AVALARA = "Avalara"

    __str__ = str.__str__


ProformaInvoiceTaxSourceTypeOrStr: TypeAlias = Annotated[
    ProformaInvoiceTaxSourceType | str, open_enum_validator(ProformaInvoiceTaxSourceType)
]
