from __future__ import annotations

from typing import TypeAlias

Quantity4: TypeAlias = str | int
"""The number of wallet units to purchase, as a decimal string with at most 8 fractional digits. Send fractional values
as strings: a JSON number with a decimal point is rejected with ``422``, because a double-precision float may already
have lost precision before the request arrives."""

Quantity4Dict: TypeAlias = str | int
