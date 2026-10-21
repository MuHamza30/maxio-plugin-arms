from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .create_prepaid_usage_component_price_point import (
    CreatePrepaidUsageComponentPricePoint,
    CreatePrepaidUsageComponentPricePointDict,
)
from .enums.credit_type import CreditTypeOrStr
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.pricing_scheme import PricingSchemeOrStr
from .overage_pricing import OveragePricing, OveragePricingDict
from .price import Price, PriceDict
from .unions.unit_price1 import UnitPrice1, UnitPrice1Dict


class PrepaidUsageComponent(SdkBaseModel):
    name: str
    """A name for this component that is suitable for showing customers and displaying on billing statements, e.g.,
    "Minutes"."""

    unit_name: str
    """The name of the unit of measurement for the component. It should be singular since it will be automatically
    pluralized when necessary. e.g., “message”, which may then be shown as “5 messages” on a subscription’s component
    line-item"""

    description: Optional[str] = UNSET
    """A description for the component that will be displayed to the user on the hosted signup page."""

    handle: Optional[str] = UNSET
    """A unique identifier for your use that can be used to retrieve this component in subsequent requests. Must start
    with a letter or number and may only contain lowercase letters, numbers, or the characters '.', ':', '-', or '_'."""

    taxable: Optional[bool] = UNSET
    """Boolean flag describing whether a component is taxable or not."""

    pricing_scheme: PricingSchemeOrStr
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    prices: Optional[list[Price]] = UNSET
    """(Not required for ‘per_unit’ pricing schemes) One or more price brackets. See `Price Bracket Rules
    <https://maxio.zendesk.com/hc/en-us/articles/24261149166733-Component-Pricing-Schemes#price-bracket-rules>`__ for an
    overview of how price brackets work for different pricing schemes."""

    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    downgrade_credit: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    price_points: Optional[list[CreatePrepaidUsageComponentPricePoint]] = UNSET
    unit_price: Optional[UnitPrice1] = UNSET
    """The amount the customer will be charged per unit when the pricing scheme is “per_unit”. For On/Off Components,
    this is the amount that the customer will be charged when they turn the component on for the subscription. The price
    can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065"""

    tax_code: Optional[str] = UNSET
    """A string representing the tax code related to the component type. This is especially important when using AvaTax
    to tax based on locale. This attribute has a max length of 25 characters."""

    hide_date_range_on_invoice: Optional[bool] = UNSET
    """(Only available on Relationship Invoicing sites) Boolean flag describing if the service date range should show
    for the component on generated invoices."""

    overage_pricing: OveragePricing
    rollover_prepaid_remainder: Optional[bool] = UNSET
    """Boolean which controls whether or not remaining units should be rolled over to the next period."""

    renew_prepaid_allocation: Optional[bool] = UNSET
    """Boolean which controls whether or not the allocated quantity should be renewed at the beginning of each
    period."""

    expiration_interval: Optional[float] = UNSET
    """(only for prepaid usage components where rollover_prepaid_remainder is true) The number of
    ``expiration_interval_unit``s after which rollover amounts should expire"""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    display_on_hosted_page: Optional[bool] = UNSET
    allow_fractional_quantities: Optional[bool] = UNSET
    public_signup_page_ids: Optional[list[int]] = UNSET
    unspsc_code: OptionalNullable[str] = UNSET
    """(Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is sent as the
    commodity code on invoice line items for this component instead of the default derived from item_category."""


class PrepaidUsageComponentDict(TypedDict):
    name: str
    unit_name: str
    description: NotRequired[str]
    handle: NotRequired[str]
    taxable: NotRequired[bool]
    pricing_scheme: PricingSchemeOrStr
    prices: NotRequired[list[PriceDict]]
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    downgrade_credit: NotRequired[CreditTypeOrStr | None]
    price_points: NotRequired[list[CreatePrepaidUsageComponentPricePointDict]]
    unit_price: NotRequired[UnitPrice1Dict]
    tax_code: NotRequired[str]
    hide_date_range_on_invoice: NotRequired[bool]
    overage_pricing: OveragePricingDict
    rollover_prepaid_remainder: NotRequired[bool]
    renew_prepaid_allocation: NotRequired[bool]
    expiration_interval: NotRequired[float]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
    display_on_hosted_page: NotRequired[bool]
    allow_fractional_quantities: NotRequired[bool]
    public_signup_page_ids: NotRequired[list[int]]
    unspsc_code: NotRequired[str | None]
