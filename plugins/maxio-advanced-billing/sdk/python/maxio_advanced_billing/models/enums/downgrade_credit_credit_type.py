from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DowngradeCreditCreditType(str, Enum):
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided. Values are:

    ``full`` - A full price credit is added for the amount owed.

    ``prorated`` - A prorated credit is added for the amount owed.

    ``none`` - No charge is added."""

    FULL = "full"
    PRORATED = "prorated"
    NONE = "none"

    __str__ = str.__str__


DowngradeCreditCreditTypeOrStr: TypeAlias = Annotated[
    DowngradeCreditCreditType | str, open_enum_validator(DowngradeCreditCreditType)
]
