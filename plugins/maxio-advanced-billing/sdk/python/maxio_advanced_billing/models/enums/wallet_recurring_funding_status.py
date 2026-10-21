from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletRecurringFundingStatus(str, Enum):
    """``active``: refilling normally. ``erroring``: the schedule is still due and retrying, but the last attempt
    couldn't be written (see ``reason``); correcting the underlying entitlement resumes funding on the next run with no
    action needed on the wallet itself. ``stopped``: funding has ended for good (see ``reason``); units already granted
    stay on the wallet and remain spendable, but no further automatic grants will be made."""

    ACTIVE = "active"
    ERRORING = "erroring"
    STOPPED = "stopped"

    __str__ = str.__str__


WalletRecurringFundingStatusOrStr: TypeAlias = Annotated[
    WalletRecurringFundingStatus | str, open_enum_validator(WalletRecurringFundingStatus)
]
