from __future__ import annotations

from typing import TypeAlias

ExpirationYear1: TypeAlias = int | str
"""(Optional when performing an Import via vault_token, required otherwise) The 4-digit credit card expiration year, as
an integer or string, e.g., 2012"""

ExpirationYear1Dict: TypeAlias = int | str
