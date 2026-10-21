from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecurringScheme(str, Enum):
    DO_NOT_RECUR = "do_not_recur"
    RECUR_INDEFINITELY = "recur_indefinitely"
    RECUR_WITH_DURATION = "recur_with_duration"

    __str__ = str.__str__


RecurringSchemeOrStr: TypeAlias = Annotated[RecurringScheme | str, open_enum_validator(RecurringScheme)]
