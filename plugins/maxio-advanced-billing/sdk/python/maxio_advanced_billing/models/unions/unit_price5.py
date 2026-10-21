from __future__ import annotations

from typing import TypeAlias

UnitPrice5: TypeAlias = str | float
"""The amount the customer will be charged per unit when the pricing scheme is “per_unit”. The price can contain up to 8
decimal places. i.e., 1.00 or 0.0012 or 0.00000065"""

UnitPrice5Dict: TypeAlias = str | float
