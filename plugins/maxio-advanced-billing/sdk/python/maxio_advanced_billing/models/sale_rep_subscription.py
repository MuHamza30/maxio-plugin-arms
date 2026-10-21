from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SaleRepSubscription(SdkBaseModel):
    id: Optional[int] = UNSET
    site_name: Optional[str] = UNSET
    subscription_url: Optional[str] = UNSET
    customer_name: Optional[str] = UNSET
    created_at: Optional[str] = UNSET
    mrr: Optional[str] = UNSET
    usage: Optional[str] = UNSET
    recurring: Optional[str] = UNSET
    last_payment: Optional[str] = UNSET
    churn_date: OptionalNullable[str] = UNSET


class SaleRepSubscriptionDict(TypedDict):
    id: NotRequired[int]
    site_name: NotRequired[str]
    subscription_url: NotRequired[str]
    customer_name: NotRequired[str]
    created_at: NotRequired[str]
    mrr: NotRequired[str]
    usage: NotRequired[str]
    recurring: NotRequired[str]
    last_payment: NotRequired[str]
    churn_date: NotRequired[str | None]
