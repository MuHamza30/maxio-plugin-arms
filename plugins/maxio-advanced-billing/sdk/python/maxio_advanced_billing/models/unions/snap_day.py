from __future__ import annotations

from typing import TypeAlias

SnapDay: TypeAlias = int | str
"""A day of month that subscription will be processed on. Can be 1 up to 28 or 'end'."""

SnapDayDict: TypeAlias = int | str
