from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DiscountType(str, Enum):
    AMOUNT = "amount"
    PERCENT = "percent"

    __str__ = str.__str__


DiscountTypeOrStr: TypeAlias = Annotated[DiscountType | str, open_enum_validator(DiscountType)]
