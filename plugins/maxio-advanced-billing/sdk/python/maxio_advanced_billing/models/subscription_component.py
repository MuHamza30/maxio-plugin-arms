from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.component_kind import ComponentKindOrStr
from .enums.credit_type import CreditTypeOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .enums.price_point_type import PricePointTypeOrStr
from .enums.pricing_scheme import PricingSchemeOrStr
from .historic_usage import HistoricUsage, HistoricUsageDict
from .subscription_component_subscription import (
    SubscriptionComponentSubscription,
    SubscriptionComponentSubscriptionDict,
)
from .unions.allocated_quantity2 import AllocatedQuantity2, AllocatedQuantity2Dict
from .unions.unit_balance1 import UnitBalance1, UnitBalance1Dict


class SubscriptionComponent(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    kind: Optional[ComponentKindOrStr] = UNSET
    """A handle for the component type"""

    unit_name: Optional[str] = UNSET
    enabled: Optional[bool] = UNSET
    """(for on/off components) indicates if the component is enabled for the subscription."""

    unit_balance: Optional[UnitBalance1] = UNSET
    currency: Optional[str] = UNSET
    allocated_quantity: Optional[AllocatedQuantity2] = UNSET
    """For Quantity-based components: The current allocation for the component on the given subscription. For On/Off
    components: Use 1 for on. Use 0 for off."""

    pricing_scheme: OptionalNullable[PricingSchemeOrStr] = UNSET
    component_id: Optional[int] = UNSET
    component_handle: OptionalNullable[str] = UNSET
    subscription_id: Optional[int] = UNSET
    recurring: Optional[bool] = UNSET
    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    downgrade_credit: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    price_point_id: OptionalNullable[int] = UNSET
    price_point_handle: OptionalNullable[str] = UNSET
    price_point_type: OptionalNullable[PricePointTypeOrStr] = UNSET
    price_point_name: OptionalNullable[str] = UNSET
    product_family_id: Optional[int] = UNSET
    product_family_handle: Optional[str] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET
    use_site_exchange_rate: OptionalNullable[bool] = UNSET
    description: OptionalNullable[str] = UNSET
    allow_fractional_quantities: Optional[bool] = UNSET
    subscription: Optional[SubscriptionComponentSubscription] = UNSET
    """(Optional) Object that will be returned if the ``include=subscription`` query param is provided."""

    historic_usages: Optional[list[HistoricUsage]] = UNSET
    display_on_hosted_page: Optional[bool] = UNSET
    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of '30' coupled with an interval_unit of day would mean this component
    price point would renew every 30 days. This property is only available for sites with Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this component price point, either month or day. This property is
    only available for sites with Multifrequency enabled."""


class SubscriptionComponentDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    kind: NotRequired[ComponentKindOrStr]
    unit_name: NotRequired[str]
    enabled: NotRequired[bool]
    unit_balance: NotRequired[UnitBalance1Dict]
    currency: NotRequired[str]
    allocated_quantity: NotRequired[AllocatedQuantity2Dict]
    pricing_scheme: NotRequired[PricingSchemeOrStr | None]
    component_id: NotRequired[int]
    component_handle: NotRequired[str | None]
    subscription_id: NotRequired[int]
    recurring: NotRequired[bool]
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    downgrade_credit: NotRequired[CreditTypeOrStr | None]
    archived_at: NotRequired[RFC3339DateTime | None]
    price_point_id: NotRequired[int | None]
    price_point_handle: NotRequired[str | None]
    price_point_type: NotRequired[PricePointTypeOrStr | None]
    price_point_name: NotRequired[str | None]
    product_family_id: NotRequired[int]
    product_family_handle: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    use_site_exchange_rate: NotRequired[bool | None]
    description: NotRequired[str | None]
    allow_fractional_quantities: NotRequired[bool]
    subscription: NotRequired[SubscriptionComponentSubscriptionDict]
    historic_usages: NotRequired[list[HistoricUsageDict]]
    display_on_hosted_page: NotRequired[bool]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
