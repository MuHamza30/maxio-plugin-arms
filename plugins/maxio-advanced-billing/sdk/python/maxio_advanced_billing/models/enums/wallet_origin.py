from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletOrigin(str, Enum):
    """How the wallet came to exist. ``manual`` for a wallet created directly with `Create Wallet
    <$e/Wallets/createWallet>`__. ``feature`` for a wallet auto-provisioned because a subscription resolved a
    usage-limit entitlement whose Feature has ``wallet_behavior`` configured."""

    MANUAL = "manual"
    FEATURE = "feature"

    __str__ = str.__str__


WalletOriginOrStr: TypeAlias = Annotated[WalletOrigin | str, open_enum_validator(WalletOrigin)]
