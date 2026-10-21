from __future__ import annotations

from typing import TypeAlias

ConversionRate: TypeAlias = str | int
"""How many wallet units one meter unit is worth, as a decimal string with at most 8 fractional digits, greater than
``0`` and below 10^16. Send fractional values as strings: a JSON number with a decimal point is rejected with ``422``,
because a double-precision float may already have lost precision before the request arrives. Only meaningful with
``meter_id``. Defaults to ``"1.0"``. Immutable once the wallet is created."""

ConversionRateDict: TypeAlias = str | int
