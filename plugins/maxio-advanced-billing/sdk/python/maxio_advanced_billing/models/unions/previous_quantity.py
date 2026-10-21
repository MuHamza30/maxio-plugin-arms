from __future__ import annotations

from typing import TypeAlias

PreviousQuantity: TypeAlias = int | str
"""The allocated quantity that was in effect before this allocation was created. String for components supporting
fractional quantities"""

PreviousQuantityDict: TypeAlias = int | str
