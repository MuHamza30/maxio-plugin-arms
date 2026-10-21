from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .component_custom_price import ComponentCustomPrice, ComponentCustomPriceDict
from .unions.allocated_quantity3 import AllocatedQuantity3, AllocatedQuantity3Dict
from .unions.component_id1 import ComponentId1, ComponentId1Dict
from .unions.price_point_id2 import PricePointId2, PricePointId2Dict
from .unions.unit_balance2 import UnitBalance2, UnitBalance2Dict


class CreateSubscriptionComponent(SdkBaseModel):
    component_id: Optional[ComponentId1] = UNSET
    enabled: Optional[bool] = UNSET
    """Used for on/off components only."""

    unit_balance: Optional[UnitBalance2] = UNSET
    """Used for metered and events based components."""

    allocated_quantity: Optional[AllocatedQuantity3] = UNSET
    """Used for quantity based components."""

    quantity: Optional[int] = UNSET
    """Deprecated. Use ``allocated_quantity`` instead."""

    price_point_id: Optional[PricePointId2] = UNSET
    custom_price: Optional[ComponentCustomPrice] = UNSET
    """Create or update custom pricing unique to the subscription. Used in place of ``price_point_id``."""


class CreateSubscriptionComponentDict(TypedDict):
    component_id: NotRequired[ComponentId1Dict]
    enabled: NotRequired[bool]
    unit_balance: NotRequired[UnitBalance2Dict]
    allocated_quantity: NotRequired[AllocatedQuantity3Dict]
    quantity: NotRequired[int]
    price_point_id: NotRequired[PricePointId2Dict]
    custom_price: NotRequired[ComponentCustomPriceDict]
