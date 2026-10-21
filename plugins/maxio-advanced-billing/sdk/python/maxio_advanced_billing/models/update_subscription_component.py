from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .component_custom_price import ComponentCustomPrice, ComponentCustomPriceDict


class UpdateSubscriptionComponent(SdkBaseModel):
    component_id: Optional[int] = UNSET
    custom_price: Optional[ComponentCustomPrice] = UNSET
    """Create or update custom pricing unique to the subscription. Used in place of ``price_point_id``."""


class UpdateSubscriptionComponentDict(TypedDict):
    component_id: NotRequired[int]
    custom_price: NotRequired[ComponentCustomPriceDict]
