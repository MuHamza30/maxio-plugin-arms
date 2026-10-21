from __future__ import annotations

from typing import TypeAlias

UnitPrice: TypeAlias = float | str
"""The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065"""

UnitPriceDict: TypeAlias = float | str
