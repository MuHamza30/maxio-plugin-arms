from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReactivationCharge(str, Enum):
    """You may choose how to handle the reactivation charge for that subscription: 1) ``prorated`` A prorated charge for
    the product price will be attempted to complete the period 2) ``immediate`` A full-price charge for the product
    price will be attempted immediately 3) ``delayed`` A full-price charge for the product price will be attempted at
    the next renewal."""

    PRORATED = "prorated"
    IMMEDIATE = "immediate"
    DELAYED = "delayed"

    __str__ = str.__str__


ReactivationChargeOrStr: TypeAlias = Annotated[ReactivationCharge | str, open_enum_validator(ReactivationCharge)]
