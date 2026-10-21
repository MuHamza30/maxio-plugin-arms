from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AllocationPreviewDirection(str, Enum):
    UPGRADE = "upgrade"
    DOWNGRADE = "downgrade"

    __str__ = str.__str__


AllocationPreviewDirectionOrStr: TypeAlias = Annotated[
    AllocationPreviewDirection | str, open_enum_validator(AllocationPreviewDirection)
]
