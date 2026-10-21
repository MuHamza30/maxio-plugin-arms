from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class HistoricUsage(SdkBaseModel):
    """(Optional) For Event Based Components. If the ``include=historic_usages`` query param is provided, the last ten
    billing periods will be returned."""

    total_usage_quantity: Optional[float] = UNSET
    """Total usage of a component for billing period"""

    billing_period_starts_at: Optional[RFC3339DateTime] = UNSET
    """Start date of billing period"""

    billing_period_ends_at: Optional[RFC3339DateTime] = UNSET
    """End date of billing period"""


class HistoricUsageDict(TypedDict):
    total_usage_quantity: NotRequired[float]
    billing_period_starts_at: NotRequired[RFC3339DateTime]
    billing_period_ends_at: NotRequired[RFC3339DateTime]
