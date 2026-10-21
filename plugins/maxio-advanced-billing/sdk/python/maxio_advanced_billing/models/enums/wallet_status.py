from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"

    __str__ = str.__str__


WalletStatusOrStr: TypeAlias = Annotated[WalletStatus | str, open_enum_validator(WalletStatus)]
