from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceRole(str, Enum):
    UNSET = "unset"
    SIGNUP = "signup"
    RENEWAL = "renewal"
    USAGE = "usage"
    REACTIVATION = "reactivation"
    PRORATION = "proration"
    MIGRATION = "migration"
    ADHOC = "adhoc"
    BACKPORT = "backport"
    BACKPORT_BALANCE_RECONCILIATION = "backport-balance-reconciliation"

    __str__ = str.__str__


InvoiceRoleOrStr: TypeAlias = Annotated[InvoiceRole | str, open_enum_validator(InvoiceRole)]
