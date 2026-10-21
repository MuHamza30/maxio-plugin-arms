from __future__ import annotations

from typing import TypeAlias

ExpirationYear2: TypeAlias = int | str
"""(Optional when performing a Subscription Import via vault_token, required otherwise) The 4-digit credit card
expiration year, as an integer or string, e.g., 2012"""

ExpirationYear2Dict: TypeAlias = int | str
