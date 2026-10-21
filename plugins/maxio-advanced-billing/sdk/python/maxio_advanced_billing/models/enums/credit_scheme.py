from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditScheme(str, Enum):
    NONE = "none"
    CREDIT = "credit"
    REFUND = "refund"

    __str__ = str.__str__


CreditSchemeOrStr: TypeAlias = Annotated[CreditScheme | str, open_enum_validator(CreditScheme)]
