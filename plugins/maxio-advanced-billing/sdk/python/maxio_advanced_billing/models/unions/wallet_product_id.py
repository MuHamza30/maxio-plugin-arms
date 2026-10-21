from __future__ import annotations

from typing import TypeAlias

WalletProductId: TypeAlias = int | str
"""The `Wallet Product <$e/Wallet%20Products/createWalletProduct>`__ that will denominate the wallet: its numeric id, or
its handle prefixed with ``handle:`` (for example ``handle:token-pack``). A bare handle with no prefix is looked up as
an id and returns ``404``. Immutable once the wallet is created."""

WalletProductIdDict: TypeAlias = int | str
