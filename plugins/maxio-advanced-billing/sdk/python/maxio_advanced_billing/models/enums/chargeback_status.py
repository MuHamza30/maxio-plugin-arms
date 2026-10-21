from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChargebackStatus(str, Enum):
    """The current chargeback status."""

    OPEN = "open"
    LOST = "lost"
    WON = "won"
    CLOSED = "closed"

    __str__ = str.__str__


ChargebackStatusOrStr: TypeAlias = Annotated[ChargebackStatus | str, open_enum_validator(ChargebackStatus)]
