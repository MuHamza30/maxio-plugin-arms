from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DebitNoteStatus(str, Enum):
    """Current status of the debit note."""

    OPEN = "open"
    APPLIED = "applied"
    BANISHED = "banished"
    PAID = "paid"

    __str__ = str.__str__


DebitNoteStatusOrStr: TypeAlias = Annotated[DebitNoteStatus | str, open_enum_validator(DebitNoteStatus)]
