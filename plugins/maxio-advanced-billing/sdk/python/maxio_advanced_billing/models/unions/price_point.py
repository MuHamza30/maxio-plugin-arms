from __future__ import annotations

from typing import TypeAlias

from ..create_component_price_point import CreateComponentPricePoint, CreateComponentPricePointDict
from ..create_prepaid_usage_component_price_point import (
    CreatePrepaidUsageComponentPricePoint,
    CreatePrepaidUsageComponentPricePointDict,
)

PricePoint: TypeAlias = CreateComponentPricePoint | CreatePrepaidUsageComponentPricePoint

PricePointDict: TypeAlias = CreateComponentPricePointDict | CreatePrepaidUsageComponentPricePointDict
