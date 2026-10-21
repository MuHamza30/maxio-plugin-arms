from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditNoteStatus(str, Enum):
    """Current status of the credit note."""

    OPEN = "open"
    APPLIED = "applied"

    __str__ = str.__str__


CreditNoteStatusOrStr: TypeAlias = Annotated[CreditNoteStatus | str, open_enum_validator(CreditNoteStatus)]
