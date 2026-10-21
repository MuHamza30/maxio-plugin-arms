from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankAccountVault(str, Enum):
    """The vault that stores the payment profile with the provided vault_token. Use ``bogus`` for testing."""

    AUTHORIZENET = "authorizenet"
    BLUE_SNAP = "blue_snap"
    BOGUS = "bogus"
    FORTE = "forte"
    GOCARDLESS = "gocardless"
    MAXIO_PAYMENTS = "maxio_payments"
    MAXP = "maxp"
    STRIPE_CONNECT = "stripe_connect"

    __str__ = str.__str__


BankAccountVaultOrStr: TypeAlias = Annotated[BankAccountVault | str, open_enum_validator(BankAccountVault)]
