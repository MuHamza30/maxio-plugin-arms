from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DebitNoteRole(str, Enum):
    """The role of the debit note."""

    CHARGEBACK = "chargeback"
    REFUND = "refund"

    __str__ = str.__str__


DebitNoteRoleOrStr: TypeAlias = Annotated[DebitNoteRole | str, open_enum_validator(DebitNoteRole)]
