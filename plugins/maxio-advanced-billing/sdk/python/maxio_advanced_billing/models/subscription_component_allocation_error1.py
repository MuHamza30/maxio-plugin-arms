from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription_component_allocation_error_item import (
    SubscriptionComponentAllocationErrorItem,
    SubscriptionComponentAllocationErrorItemDict,
)


class SubscriptionComponentAllocationError1(SdkBaseModel):
    errors: Optional[list[SubscriptionComponentAllocationErrorItem]] = UNSET


class SubscriptionComponentAllocationError1Dict(TypedDict):
    errors: NotRequired[list[SubscriptionComponentAllocationErrorItemDict]]
