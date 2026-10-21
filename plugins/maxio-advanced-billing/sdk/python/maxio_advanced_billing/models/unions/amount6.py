from __future__ import annotations

from typing import TypeAlias

Amount6: TypeAlias = str | int
"""Always positive; ``kind`` determines the sign written to the ledger. Encoded as a decimal string with at most 8
fractional digits. Send fractional values as strings: a JSON number with a decimal point is rejected with ``422``,
because a double-precision float may already have lost precision before the request arrives."""

Amount6Dict: TypeAlias = str | int
