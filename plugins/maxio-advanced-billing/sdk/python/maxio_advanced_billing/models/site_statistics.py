from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SiteStatistics(SdkBaseModel):
    total_subscriptions: Optional[int] = UNSET
    subscriptions_today: Optional[int] = UNSET
    total_revenue: Optional[str] = UNSET
    revenue_today: Optional[str] = UNSET
    revenue_this_month: Optional[str] = UNSET
    revenue_this_year: Optional[str] = UNSET
    total_canceled_subscriptions: Optional[int] = UNSET
    total_active_subscriptions: Optional[int] = UNSET
    total_past_due_subscriptions: Optional[int] = UNSET
    total_unpaid_subscriptions: Optional[int] = UNSET
    total_dunning_subscriptions: Optional[int] = UNSET


class SiteStatisticsDict(TypedDict):
    total_subscriptions: NotRequired[int]
    subscriptions_today: NotRequired[int]
    total_revenue: NotRequired[str]
    revenue_today: NotRequired[str]
    revenue_this_month: NotRequired[str]
    revenue_this_year: NotRequired[str]
    total_canceled_subscriptions: NotRequired[int]
    total_active_subscriptions: NotRequired[int]
    total_past_due_subscriptions: NotRequired[int]
    total_unpaid_subscriptions: NotRequired[int]
    total_dunning_subscriptions: NotRequired[int]
