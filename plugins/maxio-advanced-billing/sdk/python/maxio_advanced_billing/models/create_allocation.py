from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .billing_schedule import BillingSchedule, BillingScheduleDict
from .component_custom_price import ComponentCustomPrice, ComponentCustomPriceDict
from .enums.downgrade_credit_credit_type import DowngradeCreditCreditTypeOrStr
from .enums.upgrade_charge_credit_type import UpgradeChargeCreditTypeOrStr
from .unions.price_point_id1 import PricePointId1, PricePointId1Dict


class CreateAllocation(SdkBaseModel):
    quantity: float
    """The allocated quantity to which to set the line-items allocated quantity. By default, this is an integer. If
    decimal allocations are enabled for the component, it will be a decimal number. For On/Off components, use 1 for on
    and 0 for off."""

    decimal_quantity: Optional[str] = UNSET
    """Decimal representation of the allocated quantity. Only valid when decimal allocations are enabled for the
    component."""

    previous_quantity: Optional[float] = UNSET
    """The quantity that was in effect before this allocation. Responses always include this value; it may be supplied
    on preview requests to ensure the expected change is evaluated."""

    decimal_previous_quantity: Optional[str] = UNSET
    """Decimal representation of ``previous_quantity``. Only valid when decimal allocations are enabled for the
    component."""

    component_id: Optional[int] = UNSET
    """(required for the multiple allocations endpoint) The id associated with the component for which the allocation is
    being made."""

    memo: Optional[str] = UNSET
    """A memo to record along with the allocation."""

    proration_downgrade_scheme: Optional[str] = UNSET
    """The scheme used if the proration is a downgrade. Defaults to the site setting if one is not provided."""

    proration_upgrade_scheme: Optional[str] = UNSET
    """The scheme used if the proration is an upgrade. Defaults to the site setting if one is not provided."""

    downgrade_credit: OptionalNullable[DowngradeCreditCreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided. Values are:

    ``full`` - A full price credit is added for the amount owed.

    ``prorated`` - A prorated credit is added for the amount owed.

    ``none`` - No charge is added."""

    upgrade_charge: OptionalNullable[UpgradeChargeCreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided. Values are:

    ``full`` - A charge is added for the full price of the component.

    ``prorated`` - A charge is added for the prorated price of the component change.

    ``none`` - No charge is added."""

    accrue_charge: Optional[bool] = UNSET
    """"If the change in cost is an upgrade, this determines if the charge should accrue to the next renewal or if
    capture should be attempted immediately.

    ``true`` - Attempt to charge the customer at the next renewal.

    ``false`` - Attempt to charge the customer right away. If it fails, the charge will be accrued until the next
    renewal.

    Defaults to the site setting if unspecified in the request."""

    initiate_dunning: Optional[bool] = UNSET
    """If set to true, if the immediate component payment fails, initiate dunning for the subscription. Otherwise, leave
    the charges on the subscription to pay for at renewal. Defaults to false."""

    price_point_id: OptionalNullable[PricePointId1] = UNSET
    """Price point that the allocation should be charged at. Accepts either the price point's id (integer) or handle
    (string). When not specified, the default price point will be used."""

    billing_schedule: Optional[BillingSchedule] = UNSET
    """Billing schedule settings for component allocations or usages on multi-frequency subscriptions. Use this to start
    a component's billing period on a custom date instead of aligning with the product charge schedule."""

    custom_price: Optional[ComponentCustomPrice] = UNSET
    """Create or update custom pricing unique to the subscription. Used in place of ``price_point_id``."""


class CreateAllocationDict(TypedDict):
    quantity: float
    decimal_quantity: NotRequired[str]
    previous_quantity: NotRequired[float]
    decimal_previous_quantity: NotRequired[str]
    component_id: NotRequired[int]
    memo: NotRequired[str]
    proration_downgrade_scheme: NotRequired[str]
    proration_upgrade_scheme: NotRequired[str]
    downgrade_credit: NotRequired[DowngradeCreditCreditTypeOrStr | None]
    upgrade_charge: NotRequired[UpgradeChargeCreditTypeOrStr | None]
    accrue_charge: NotRequired[bool]
    initiate_dunning: NotRequired[bool]
    price_point_id: NotRequired[PricePointId1Dict | None]
    billing_schedule: NotRequired[BillingScheduleDict]
    custom_price: NotRequired[ComponentCustomPriceDict]
