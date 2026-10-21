from __future__ import annotations

from typing import TypeAlias

PricePointId3: TypeAlias = str | int
"""Either the component price point's Chargify id or its handle prefixed with ``handle:``"""

PricePointId3Dict: TypeAlias = str | int
