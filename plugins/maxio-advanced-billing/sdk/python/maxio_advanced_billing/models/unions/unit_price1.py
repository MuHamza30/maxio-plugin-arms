from __future__ import annotations

from typing import TypeAlias

UnitPrice1: TypeAlias = str | float
"""The amount the customer will be charged per unit when the pricing scheme is “per_unit”. For On/Off Components, this
is the amount that the customer will be charged when they turn the component on for the subscription. The price can
contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065"""

UnitPrice1Dict: TypeAlias = str | float
