from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AutoInvite(int, Enum):
    VALUE_0 = 0
    """Do not send the invitation email."""

    VALUE_1 = 1
    """Automatically send the invitation email."""

    __str__ = str.__str__


AutoInviteOrInt: TypeAlias = Annotated[AutoInvite | int, open_enum_validator(AutoInvite)]
