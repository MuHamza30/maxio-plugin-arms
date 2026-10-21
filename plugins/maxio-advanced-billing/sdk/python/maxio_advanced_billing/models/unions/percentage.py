from __future__ import annotations

from typing import TypeAlias

Percentage: TypeAlias = str | float
"""Required when creating a new percentage coupon. Can't be used together with amount_in_cents. Percentage discount."""

PercentageDict: TypeAlias = str | float
