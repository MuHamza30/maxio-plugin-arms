from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mrr_movement import MrrMovement, MrrMovementDict


class MovementLineItem(SdkBaseModel):
    product_id: Optional[int] = UNSET
    component_id: Optional[int] = UNSET
    """For Product (or "baseline") line items, this field will have a value of ``0``."""

    price_point_id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    mrr: Optional[int] = UNSET
    mrr_movements: Optional[list[MrrMovement]] = UNSET
    quantity: Optional[int] = UNSET
    prev_quantity: Optional[int] = UNSET
    recurring: Optional[bool] = UNSET
    """When ``true``, the line item's MRR value will contribute to the ``plan`` breakout. When ``false``, the line item
    contributes to the ``usage`` breakout."""


class MovementLineItemDict(TypedDict):
    product_id: NotRequired[int]
    component_id: NotRequired[int]
    price_point_id: NotRequired[int]
    name: NotRequired[str]
    mrr: NotRequired[int]
    mrr_movements: NotRequired[list[MrrMovementDict]]
    quantity: NotRequired[int]
    prev_quantity: NotRequired[int]
    recurring: NotRequired[bool]
