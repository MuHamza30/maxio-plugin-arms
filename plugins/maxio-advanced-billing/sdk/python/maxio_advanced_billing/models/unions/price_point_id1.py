from __future__ import annotations

from typing import TypeAlias

PricePointId1: TypeAlias = str | int
"""Price point that the allocation should be charged at. Accepts either the price point's id (integer) or handle
(string). When not specified, the default price point will be used."""

PricePointId1Dict: TypeAlias = str | int
