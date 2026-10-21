from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Origin(str, Enum):
    """How the grant was created. ``recurring`` comes from the wallet's automatic funding schedule (see the wallet's
    ``recurring_funding`` array). ``manual`` comes from a one-time grant posted to `Create Wallet Transaction
    <$e/Wallet%20Transactions/createWalletTransaction>`__. ``initial_balance`` comes from a non-zero ``initial_balance``
    at wallet creation. ``allowance_increase`` comes from raising a funding entitlement's allowance while it's already
    funding a wallet. ``purchase`` comes from `Create Wallet Purchase
    <$e/Wallet%20Purchases/createWalletPurchase>`__."""

    RECURRING = "recurring"
    MANUAL = "manual"
    INITIAL_BALANCE = "initial_balance"
    ALLOWANCE_INCREASE = "allowance_increase"
    PURCHASE = "purchase"

    __str__ = str.__str__


OriginOrStr: TypeAlias = Annotated[Origin | str, open_enum_validator(Origin)]
