from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResumptionCharge(str, Enum):
    """(For calendar billing subscriptions only) The way that the resumed subscription's charge should be handled"""

    PRORATED = "prorated"
    IMMEDIATE = "immediate"
    DELAYED = "delayed"

    __str__ = str.__str__


ResumptionChargeOrStr: TypeAlias = Annotated[ResumptionCharge | str, open_enum_validator(ResumptionCharge)]
