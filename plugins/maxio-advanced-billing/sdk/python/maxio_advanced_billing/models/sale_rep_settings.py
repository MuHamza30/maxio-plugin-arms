from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaleRepSettings(SdkBaseModel):
    customer_name: Optional[str] = UNSET
    subscription_id: Optional[int] = UNSET
    site_link: Optional[str] = UNSET
    site_name: Optional[str] = UNSET
    subscription_mrr: Optional[str] = UNSET
    sales_rep_id: Optional[int] = UNSET
    sales_rep_name: Optional[str] = UNSET


class SaleRepSettingsDict(TypedDict):
    customer_name: NotRequired[str]
    subscription_id: NotRequired[int]
    site_link: NotRequired[str]
    site_name: NotRequired[str]
    subscription_mrr: NotRequired[str]
    sales_rep_id: NotRequired[int]
    sales_rep_name: NotRequired[str]
