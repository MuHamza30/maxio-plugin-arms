from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .site_statistics import SiteStatistics, SiteStatisticsDict


class SiteSummary(SdkBaseModel):
    seller_name: Optional[str] = UNSET
    site_name: Optional[str] = UNSET
    site_id: Optional[int] = UNSET
    site_currency: Optional[str] = UNSET
    stats: Optional[SiteStatistics] = UNSET


class SiteSummaryDict(TypedDict):
    seller_name: NotRequired[str]
    site_name: NotRequired[str]
    site_id: NotRequired[int]
    site_currency: NotRequired[str]
    stats: NotRequired[SiteStatisticsDict]
