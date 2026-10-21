from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UpgradeChargeCreditType(str, Enum):
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided. Values are:

    ``full`` - A charge is added for the full price of the component.

    ``prorated`` - A charge is added for the prorated price of the component change.

    ``none`` - No charge is added."""

    FULL = "full"
    PRORATED = "prorated"
    NONE = "none"

    __str__ = str.__str__


UpgradeChargeCreditTypeOrStr: TypeAlias = Annotated[
    UpgradeChargeCreditType | str, open_enum_validator(UpgradeChargeCreditType)
]
