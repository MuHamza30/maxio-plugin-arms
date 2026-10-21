from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CollectionMethod(str, Enum):
    """The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options
    are - ``invoice``, ``automatic``. For current Relationship Invoicing Architecture valid options are -
    ``remittance``, ``automatic``, ``prepaid``."""

    AUTOMATIC = "automatic"
    REMITTANCE = "remittance"
    PREPAID = "prepaid"
    INVOICE = "invoice"

    __str__ = str.__str__


CollectionMethodOrStr: TypeAlias = Annotated[CollectionMethod | str, open_enum_validator(CollectionMethod)]
