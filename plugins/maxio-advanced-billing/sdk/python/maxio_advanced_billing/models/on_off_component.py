from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .component_price_point_item import ComponentPricePointItem, ComponentPricePointItemDict
from .enums.credit_type import CreditTypeOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .unions.unit_price3 import UnitPrice3, UnitPrice3Dict


class OnOffComponent(SdkBaseModel):
    name: str
    """A name for this component that is suitable for showing customers and displaying on billing statements, e.g.,
    "Minutes"."""

    description: Optional[str] = UNSET
    """A description for the component that will be displayed to the user on the hosted signup page."""

    handle: Optional[str] = UNSET
    """A unique identifier for your use that can be used to retrieve this component in subsequent requests. Must start
    with a letter or number and may only contain lowercase letters, numbers, or the characters '.', ':', '-', or '_'."""

    taxable: Optional[bool] = UNSET
    """Boolean flag describing whether a component is taxable or not."""

    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    downgrade_credit: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    price_points: Optional[list[ComponentPricePointItem]] = UNSET
    unit_price: UnitPrice3
    """This is the amount that the customer will be charged when they turn the component on for the subscription. The
    price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065"""

    tax_code: Optional[str] = UNSET
    """A string representing the tax code related to the component type. This is especially important when using AvaTax
    to tax based on locale. This attribute has a max length of 25 characters."""

    hide_date_range_on_invoice: Optional[bool] = UNSET
    """(Only available on Relationship Invoicing sites) Boolean flag describing if the service date range should show
    for the component on generated invoices."""

    display_on_hosted_page: Optional[bool] = UNSET
    allow_fractional_quantities: Optional[bool] = UNSET
    public_signup_page_ids: Optional[list[int]] = UNSET
    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this
    component's default price point would renew every 30 days. This property is only available for sites with
    Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this component's default price point, either month or day. This
    property is only available for sites with Multifrequency enabled."""

    unspsc_code: OptionalNullable[str] = UNSET
    """(Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is sent as the
    commodity code on invoice line items for this component instead of the default derived from item_category."""


class OnOffComponentDict(TypedDict):
    name: str
    description: NotRequired[str]
    handle: NotRequired[str]
    taxable: NotRequired[bool]
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    downgrade_credit: NotRequired[CreditTypeOrStr | None]
    price_points: NotRequired[list[ComponentPricePointItemDict]]
    unit_price: UnitPrice3Dict
    tax_code: NotRequired[str]
    hide_date_range_on_invoice: NotRequired[bool]
    display_on_hosted_page: NotRequired[bool]
    allow_fractional_quantities: NotRequired[bool]
    public_signup_page_ids: NotRequired[list[int]]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
    unspsc_code: NotRequired[str | None]
