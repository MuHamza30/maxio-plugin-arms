from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ScheduledRenewalConfigurationItem(SdkBaseModel):
    id: Optional[int] = UNSET
    subscription_id: Optional[int] = UNSET
    subscription_renewal_configuration_id: Optional[int] = UNSET
    item_id: Optional[int] = UNSET
    item_type: Optional[str] = UNSET
    item_subclass: Optional[str] = UNSET
    price_point_id: Optional[int] = UNSET
    price_point_type: Optional[str] = UNSET
    quantity: Optional[int] = UNSET
    decimal_quantity: Optional[str] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET


class ScheduledRenewalConfigurationItemDict(TypedDict):
    id: NotRequired[int]
    subscription_id: NotRequired[int]
    subscription_renewal_configuration_id: NotRequired[int]
    item_id: NotRequired[int]
    item_type: NotRequired[str]
    item_subclass: NotRequired[str]
    price_point_id: NotRequired[int]
    price_point_type: NotRequired[str]
    quantity: NotRequired[int]
    decimal_quantity: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
