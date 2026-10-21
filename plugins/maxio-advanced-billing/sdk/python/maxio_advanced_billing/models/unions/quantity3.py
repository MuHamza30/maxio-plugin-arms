from __future__ import annotations

from typing import TypeAlias

Quantity3: TypeAlias = float | str
"""The quantity can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065. If you submit a value with more
than 8 decimal places, we will round it down to the 8th decimal place."""

Quantity3Dict: TypeAlias = float | str
