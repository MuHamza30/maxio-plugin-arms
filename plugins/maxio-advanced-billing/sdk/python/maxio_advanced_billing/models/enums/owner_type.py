from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OwnerType(str, Enum):
    """The polymorphic owner type. ``subscription`` is the only value currently supported."""

    SUBSCRIPTION = "subscription"

    __str__ = str.__str__


OwnerTypeOrStr: TypeAlias = Annotated[OwnerType | str, open_enum_validator(OwnerType)]
