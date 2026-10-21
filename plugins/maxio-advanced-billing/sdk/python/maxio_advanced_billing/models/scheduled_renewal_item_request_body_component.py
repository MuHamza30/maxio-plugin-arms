from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scheduled_renewal_component_custom_price import (
    ScheduledRenewalComponentCustomPrice,
    ScheduledRenewalComponentCustomPriceDict,
)


class ScheduledRenewalItemRequestBodyComponent(SdkBaseModel):
    item_type: Literal["Component"] = "Component"
    """Item type to add. Either Product or Component."""

    item_id: int
    """Product or component identifier."""

    price_point_id: Optional[int] = UNSET
    """Price point identifier."""

    quantity: Optional[int] = UNSET
    """(Optional) Quantity for the item."""

    custom_price: Optional[ScheduledRenewalComponentCustomPrice] = UNSET
    """Custom pricing for a component within a scheduled renewal."""


class ScheduledRenewalItemRequestBodyComponentDict(TypedDict):
    item_type: Literal["Component"]
    item_id: int
    price_point_id: NotRequired[int]
    quantity: NotRequired[int]
    custom_price: NotRequired[ScheduledRenewalComponentCustomPriceDict]
