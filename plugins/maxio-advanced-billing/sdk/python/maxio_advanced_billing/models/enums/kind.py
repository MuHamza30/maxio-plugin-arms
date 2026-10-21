from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Kind(str, Enum):
    ACCESS_RIGHT = "access_right"
    USAGE_LIMIT = "usage_limit"
    SERVICE_RIGHT = "service_right"
    ALL = "all"

    __str__ = str.__str__


KindOrStr: TypeAlias = Annotated[Kind | str, open_enum_validator(Kind)]
