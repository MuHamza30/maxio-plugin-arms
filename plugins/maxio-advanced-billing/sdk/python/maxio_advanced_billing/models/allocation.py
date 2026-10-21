from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.credit_type import CreditTypeOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .payment_for_allocation import PaymentForAllocation, PaymentForAllocationDict
from .unions.previous_quantity import PreviousQuantity, PreviousQuantityDict
from .unions.quantity import Quantity, QuantityDict


class Allocation(SdkBaseModel):
    allocation_id: Optional[int] = UNSET
    """The allocation unique ID"""

    component_id: Optional[int] = UNSET
    """The integer component ID for the allocation. This references a component that you have created in your Product
    setup."""

    component_handle: OptionalNullable[str] = UNSET
    """The handle of the component. This references a component that you have created in your Product setup."""

    subscription_id: Optional[int] = UNSET
    """The integer subscription ID for the allocation. This references a unique subscription in your Site."""

    quantity: Optional[Quantity] = UNSET
    """The allocated quantity set into effect by the allocation. String for components supporting fractional
    quantities"""

    previous_quantity: Optional[PreviousQuantity] = UNSET
    """The allocated quantity that was in effect before this allocation was created. String for components supporting
    fractional quantities"""

    memo: OptionalNullable[str] = UNSET
    """The memo passed when the allocation was created"""

    timestamp: Optional[RFC3339DateTime] = UNSET
    """The time that the allocation was recorded, in ISO 8601 format and UTC timezone, e.g., 2012-11-20T22:00:37Z"""

    created_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when this allocation was created"""

    proration_upgrade_scheme: Optional[str] = UNSET
    """The scheme used if the proration was an upgrade. This is only present when the allocation was created
    mid-period."""

    proration_downgrade_scheme: Optional[str] = UNSET
    """The scheme used if the proration was a downgrade. This is only present when the allocation was created
    mid-period."""

    price_point_id: Optional[int] = UNSET
    price_point_name: Optional[str] = UNSET
    price_point_handle: Optional[str] = UNSET
    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this component
    price point would renew every 30 days. This property is only available for sites with Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this component price point, either month or day. This property is
    only available for sites with Multifrequency enabled."""

    previous_price_point_id: Optional[int] = UNSET
    accrue_charge: Optional[bool] = UNSET
    """If the change in cost is an upgrade, this determines if the charge should accrue to the next renewal or if
    capture should be attempted immediately."""

    initiate_dunning: Optional[bool] = UNSET
    """If true, if the immediate component payment fails, initiate dunning for the subscription. Otherwise, leave the
    charges on the subscription to pay for at renewal."""

    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    downgrade_credit: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    payment: OptionalNullable[PaymentForAllocation] = UNSET
    expires_at: Optional[RFC3339DateTime] = UNSET
    used_quantity: Optional[int] = UNSET
    charge_id: Optional[int] = UNSET


class AllocationDict(TypedDict):
    allocation_id: NotRequired[int]
    component_id: NotRequired[int]
    component_handle: NotRequired[str | None]
    subscription_id: NotRequired[int]
    quantity: NotRequired[QuantityDict]
    previous_quantity: NotRequired[PreviousQuantityDict]
    memo: NotRequired[str | None]
    timestamp: NotRequired[RFC3339DateTime]
    created_at: NotRequired[RFC3339DateTime]
    proration_upgrade_scheme: NotRequired[str]
    proration_downgrade_scheme: NotRequired[str]
    price_point_id: NotRequired[int]
    price_point_name: NotRequired[str]
    price_point_handle: NotRequired[str]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
    previous_price_point_id: NotRequired[int]
    accrue_charge: NotRequired[bool]
    initiate_dunning: NotRequired[bool]
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    downgrade_credit: NotRequired[CreditTypeOrStr | None]
    payment: NotRequired[PaymentForAllocationDict | None]
    expires_at: NotRequired[RFC3339DateTime]
    used_quantity: NotRequired[int]
    charge_id: NotRequired[int]
