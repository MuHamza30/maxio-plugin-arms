from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceCreditType(str, Enum):
    """The type of entry"""

    CREDIT = "Credit"
    DEBIT = "Debit"

    __str__ = str.__str__


ServiceCreditTypeOrStr: TypeAlias = Annotated[ServiceCreditType | str, open_enum_validator(ServiceCreditType)]
