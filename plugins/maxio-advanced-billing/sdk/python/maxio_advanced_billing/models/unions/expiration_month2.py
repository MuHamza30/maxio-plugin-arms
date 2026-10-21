from __future__ import annotations

from typing import TypeAlias

ExpirationMonth2: TypeAlias = int | str
"""(Optional when performing a Subscription Import via vault_token, required otherwise) The 1- or 2-digit credit card
expiration month, as an integer or string, e.g., 5"""

ExpirationMonth2Dict: TypeAlias = int | str
