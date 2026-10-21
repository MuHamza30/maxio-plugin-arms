from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditType(str, Enum):
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    FULL = "full"
    PRORATED = "prorated"
    NONE = "none"

    __str__ = str.__str__


CreditTypeOrStr: TypeAlias = Annotated[CreditType | str, open_enum_validator(CreditType)]
