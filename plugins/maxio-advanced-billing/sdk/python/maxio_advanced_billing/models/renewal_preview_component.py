from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.component_id2 import ComponentId2, ComponentId2Dict
from .unions.price_point_id3 import PricePointId3, PricePointId3Dict


class RenewalPreviewComponent(SdkBaseModel):
    component_id: Optional[ComponentId2] = UNSET
    """Either the component's Chargify id or its handle prefixed with ``handle:``"""

    quantity: Optional[int] = UNSET
    """The quantity for which you wish to preview billing. This is useful if you want to preview a predicted, higher
    usage value than is currently present on the subscription.

    This quantity represents:

    - Whether or not an on/off component is enabled - use 0 for disabled or 1 for enabled
    - The desired allocated_quantity for a quantity-based component
    - The desired unit_balance for a metered component
    - The desired metric quantity for an events-based component"""

    price_point_id: Optional[PricePointId3] = UNSET
    """Either the component price point's Chargify id or its handle prefixed with ``handle:``"""


class RenewalPreviewComponentDict(TypedDict):
    component_id: NotRequired[ComponentId2Dict]
    quantity: NotRequired[int]
    price_point_id: NotRequired[PricePointId3Dict]
