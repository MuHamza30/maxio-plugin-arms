from __future__ import annotations

from typing import TypeAlias

InitialBalance: TypeAlias = str | int
"""(Optional) A free opening balance, not a purchase and not reflected on any invoice. When non-zero, wallet creation
also writes an initial-balance grant and a matching ``initial_balance`` ledger row. Omitted or exactly ``0`` creates a
zero-balance wallet, not an error. Encoded as a decimal string with at most 8 fractional digits, and must be
non-negative and below 10^16. Send fractional values as strings: a JSON number with a decimal point is rejected with
``422``, because a double-precision float may already have lost precision before the request arrives."""

InitialBalanceDict: TypeAlias = str | int
