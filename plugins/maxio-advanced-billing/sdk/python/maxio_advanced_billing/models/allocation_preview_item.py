from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.credit_type import CreditTypeOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .unions.previous_quantity1 import PreviousQuantity1, PreviousQuantity1Dict
from .unions.quantity1 import Quantity1, Quantity1Dict


class AllocationPreviewItem(SdkBaseModel):
    component_id: Optional[int] = UNSET
    subscription_id: Optional[int] = UNSET
    quantity: Optional[Quantity1] = UNSET
    previous_quantity: Optional[PreviousQuantity1] = UNSET
    memo: OptionalNullable[str] = UNSET
    timestamp: OptionalNullable[str] = UNSET
    proration_upgrade_scheme: Optional[str] = UNSET
    proration_downgrade_scheme: Optional[str] = UNSET
    accrue_charge: Optional[bool] = UNSET
    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    downgrade_credit: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    price_point_id: Optional[int] = UNSET
    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this component
    price point would renew every 30 days. This property is only available for sites with Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this component price point, either month or day. This property is
    only available for sites with Multifrequency enabled."""

    previous_price_point_id: Optional[int] = UNSET
    price_point_handle: Optional[str] = UNSET
    price_point_name: Optional[str] = UNSET
    component_handle: OptionalNullable[str] = UNSET


class AllocationPreviewItemDict(TypedDict):
    component_id: NotRequired[int]
    subscription_id: NotRequired[int]
    quantity: NotRequired[Quantity1Dict]
    previous_quantity: NotRequired[PreviousQuantity1Dict]
    memo: NotRequired[str | None]
    timestamp: NotRequired[str | None]
    proration_upgrade_scheme: NotRequired[str]
    proration_downgrade_scheme: NotRequired[str]
    accrue_charge: NotRequired[bool]
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    downgrade_credit: NotRequired[CreditTypeOrStr | None]
    price_point_id: NotRequired[int]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
    previous_price_point_id: NotRequired[int]
    price_point_handle: NotRequired[str]
    price_point_name: NotRequired[str]
    component_handle: NotRequired[str | None]
