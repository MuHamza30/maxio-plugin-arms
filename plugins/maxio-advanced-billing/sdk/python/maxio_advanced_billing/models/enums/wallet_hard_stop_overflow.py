from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletHardStopOverflow(str, Enum):
    """Behavior at the hard-stop boundary. ``discard`` drains the wallet to zero and rejects the excess (the default).
    ``allow_negative`` deducts the full amount, letting the balance go negative. The excess past the wallet's grants is
    booked as an overdraft ledger row with ``grant_id`` set to ``null``."""

    DISCARD = "discard"
    ALLOW_NEGATIVE = "allow_negative"

    __str__ = str.__str__


WalletHardStopOverflowOrStr: TypeAlias = Annotated[
    WalletHardStopOverflow | str, open_enum_validator(WalletHardStopOverflow)
]
