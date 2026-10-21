from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceDiscountType(str, Enum):
    PERCENTAGE = "percentage"
    FLAT_AMOUNT = "flat_amount"
    ROLLOVER = "rollover"

    __str__ = str.__str__


InvoiceDiscountTypeOrStr: TypeAlias = Annotated[InvoiceDiscountType | str, open_enum_validator(InvoiceDiscountType)]
