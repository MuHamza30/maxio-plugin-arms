from __future__ import annotations

from typing import TypeAlias

AllocatedQuantity2: TypeAlias = int | str
"""For Quantity-based components: The current allocation for the component on the given subscription. For On/Off
components: Use 1 for on. Use 0 for off."""

AllocatedQuantity2Dict: TypeAlias = int | str
