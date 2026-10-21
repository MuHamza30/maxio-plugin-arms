from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayPalVault(str, Enum):
    """The vault that stores the payment profile with the provided vault_token."""

    BRAINTREE_BLUE = "braintree_blue"
    PAYPAL = "paypal"
    MODUSLINK = "moduslink"
    PAYPAL_COMPLETE = "paypal_complete"

    __str__ = str.__str__


PayPalVaultOrStr: TypeAlias = Annotated[PayPalVault | str, open_enum_validator(PayPalVault)]
