from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankAccountHolderType(str, Enum):
    """Defaults to personal"""

    PERSONAL = "personal"
    BUSINESS = "business"

    __str__ = str.__str__


BankAccountHolderTypeOrStr: TypeAlias = Annotated[
    BankAccountHolderType | str, open_enum_validator(BankAccountHolderType)
]
