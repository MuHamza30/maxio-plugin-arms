from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription_group_component_custom_price import (
    SubscriptionGroupComponentCustomPrice,
    SubscriptionGroupComponentCustomPriceDict,
)
from .unions.allocated_quantity1 import AllocatedQuantity1, AllocatedQuantity1Dict
from .unions.component_id import ComponentId, ComponentIdDict
from .unions.price_point_id import PricePointId, PricePointIdDict
from .unions.unit_balance import UnitBalance, UnitBalanceDict


class SubscriptionGroupSignupComponent(SdkBaseModel):
    component_id: Optional[ComponentId] = UNSET
    """Required if passing any component to ``components`` attribute."""

    allocated_quantity: Optional[AllocatedQuantity1] = UNSET
    unit_balance: Optional[UnitBalance] = UNSET
    price_point_id: Optional[PricePointId] = UNSET
    custom_price: Optional[SubscriptionGroupComponentCustomPrice] = UNSET
    """Used in place of ``price_point_id`` to define a custom price point unique to the subscription. You still need to
    provide ``component_id``."""


class SubscriptionGroupSignupComponentDict(TypedDict):
    component_id: NotRequired[ComponentIdDict]
    allocated_quantity: NotRequired[AllocatedQuantity1Dict]
    unit_balance: NotRequired[UnitBalanceDict]
    price_point_id: NotRequired[PricePointIdDict]
    custom_price: NotRequired[SubscriptionGroupComponentCustomPriceDict]
