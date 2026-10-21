from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ApplePayVault(str, Enum):
    """The vault that stores the payment profile with the provided vault_token."""

    BRAINTREE_BLUE = "braintree_blue"

    __str__ = str.__str__


ApplePayVaultOrStr: TypeAlias = Annotated[ApplePayVault | str, open_enum_validator(ApplePayVault)]
