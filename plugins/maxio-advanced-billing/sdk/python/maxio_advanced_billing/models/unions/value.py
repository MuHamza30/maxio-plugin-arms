from __future__ import annotations

from typing import TypeAlias

Value: TypeAlias = bool | float | str
"""The aggregated value, coerced according to ``type``: a boolean for ``access_right`` (and boolean ``service_right``),
a number for ``usage_limit`` (and numeric ``service_right``), or a string for text ``service_right``."""

ValueDict: TypeAlias = bool | float | str
