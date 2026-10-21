from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_schedule import BillingSchedule, BillingScheduleDict
from .component_custom_price import ComponentCustomPrice, ComponentCustomPriceDict


class CreateUsage(SdkBaseModel):
    quantity: Optional[float] = UNSET
    """integer by default or decimal number if fractional quantities are enabled for the component"""

    price_point_id: Optional[str] = UNSET
    memo: Optional[str] = UNSET
    billing_schedule: Optional[BillingSchedule] = UNSET
    """Billing schedule settings for component allocations or usages on multi-frequency subscriptions. Use this to start
    a component's billing period on a custom date instead of aligning with the product charge schedule."""

    custom_price: Optional[ComponentCustomPrice] = UNSET
    """Create or update custom pricing unique to the subscription. Used in place of ``price_point_id``."""


class CreateUsageDict(TypedDict):
    quantity: NotRequired[float]
    price_point_id: NotRequired[str]
    memo: NotRequired[str]
    billing_schedule: NotRequired[BillingScheduleDict]
    custom_price: NotRequired[ComponentCustomPriceDict]
