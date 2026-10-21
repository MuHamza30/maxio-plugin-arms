from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .component_price import ComponentPrice, ComponentPriceDict
from .enums.component_kind import ComponentKindOrStr
from .enums.credit_type import CreditTypeOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .enums.item_category import ItemCategoryOrStr
from .enums.pricing_scheme import PricingSchemeOrStr
from .feature_catalog_item import FeatureCatalogItem, FeatureCatalogItemDict
from .wallet_product_price_point_summary import WalletProductPricePointSummary, WalletProductPricePointSummaryDict
from .wallet_product_usage_count import WalletProductUsageCount, WalletProductUsageCountDict


class WalletProductListItem(SdkBaseModel):
    """A Wallet Product as it appears in `List Wallet Products <$e/Wallet%20Products/listWalletProducts>`__: the full
    Component field set, plus a usage count and a price point summary that only the list response reports."""

    id: Optional[int] = UNSET
    """The unique ID assigned to the component by Chargify. This ID can be used to fetch the component from the API."""

    name: Optional[str] = UNSET
    """The name of the Component, suitable for display on statements. e.g., Text Messages."""

    handle: OptionalNullable[str] = UNSET
    """The component API handle"""

    pricing_scheme: OptionalNullable[PricingSchemeOrStr] = UNSET
    unit_name: Optional[str] = UNSET
    """The name of the unit that the component’s usage is measured in. e.g., message"""

    unit_price: OptionalNullable[str] = UNSET
    """The amount the customer will be charged per unit. This field is only populated for ‘per_unit’ pricing schemes,
    otherwise it may be null."""

    product_family_id: OptionalNullable[int] = UNSET
    """The id of the Product Family to which the Component belongs. ``null`` for a Wallet Product, which has no Product
    Family."""

    product_family_name: OptionalNullable[str] = UNSET
    """The name of the Product Family to which the Component belongs. ``null`` for a Wallet Product, which has no
    Product Family."""

    product_family_handle: OptionalNullable[str] = UNSET
    """The handle of the Product Family to which the Component belongs. ``null`` for a Wallet Product, which has no
    Product Family."""

    price_per_unit_in_cents: OptionalNullable[int] = UNSET
    """deprecated - use unit_price instead."""

    kind: Optional[ComponentKindOrStr] = UNSET
    """A handle for the component type"""

    archived: Optional[bool] = UNSET
    """Boolean flag describing whether a component is archived or not."""

    description: OptionalNullable[str] = UNSET
    """The description of the component."""

    default_price_point_id: OptionalNullable[int] = UNSET
    overage_prices: OptionalNullable[list[ComponentPrice]] = UNSET
    """Applicable only to prepaid usage components. An array of overage price brackets."""

    prices: OptionalNullable[list[ComponentPrice]] = UNSET
    """An array of price brackets. If the component uses the ‘per_unit’ pricing scheme, this array will be empty."""

    price_point_count: Optional[int] = UNSET
    """Count for the number of price points associated with the component"""

    price_points_url: OptionalNullable[str] = UNSET
    """URL that points to the location to read the existing price points via GET request"""

    default_price_point_name: Optional[str] = UNSET
    taxable: Optional[bool] = UNSET
    """Boolean flag describing whether a component is taxable or not."""

    tax_code: OptionalNullable[str] = UNSET
    """A string representing the tax code related to the component type. This is especially important when using AvaTax
    to tax based on locale. This attribute has a max length of 25 characters."""

    recurring: Optional[bool] = UNSET
    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    downgrade_credit: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    created_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when this component was created"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when this component was updated"""

    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp indicating when this component was archived"""

    hide_date_range_on_invoice: Optional[bool] = UNSET
    """(Only available on Relationship Invoicing sites) Boolean flag describing if the service date range should show
    for the component on generated invoices."""

    allow_fractional_quantities: Optional[bool] = UNSET
    item_category: OptionalNullable[ItemCategoryOrStr] = UNSET
    """One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other"""

    use_site_exchange_rate: OptionalNullable[bool] = UNSET
    accounting_code: OptionalNullable[str] = UNSET
    """E.g. Internal ID or SKU Number"""

    event_based_billing_metric_id: Optional[int] = UNSET
    """(Only for Event Based Components) This is an ID of a metric attached to the component. This metric is used to
    bill upon collected events."""

    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this
    component’s default price point would renew every 30 days. This property is only available for sites with
    Multifrequency enabled."""

    interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this component's default price point, either month or day. This
    property is only available for sites with Multifrequency enabled."""

    unspsc_code: OptionalNullable[str] = UNSET
    """(Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is sent as the
    commodity code on invoice line items for this component instead of the default derived from item_category."""

    features: OptionalNullable[list[FeatureCatalogItem]] = UNSET
    """The active feature catalog items attached to this component. Present only when the request includes
    ``include_features=true``."""

    used_by: Optional[WalletProductUsageCount] = UNSET
    """A rollup of what's using this Wallet Product, for the catalog listing."""

    price_point_summary: Optional[WalletProductPricePointSummary] = UNSET
    """A summary of the Wallet Product's default price point, for rendering a catalog listing without a separate price
    points call."""


class WalletProductListItemDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    handle: NotRequired[str | None]
    pricing_scheme: NotRequired[PricingSchemeOrStr | None]
    unit_name: NotRequired[str]
    unit_price: NotRequired[str | None]
    product_family_id: NotRequired[int | None]
    product_family_name: NotRequired[str | None]
    product_family_handle: NotRequired[str | None]
    price_per_unit_in_cents: NotRequired[int | None]
    kind: NotRequired[ComponentKindOrStr]
    archived: NotRequired[bool]
    description: NotRequired[str | None]
    default_price_point_id: NotRequired[int | None]
    overage_prices: NotRequired[list[ComponentPriceDict] | None]
    prices: NotRequired[list[ComponentPriceDict] | None]
    price_point_count: NotRequired[int]
    price_points_url: NotRequired[str | None]
    default_price_point_name: NotRequired[str]
    taxable: NotRequired[bool]
    tax_code: NotRequired[str | None]
    recurring: NotRequired[bool]
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    downgrade_credit: NotRequired[CreditTypeOrStr | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    archived_at: NotRequired[RFC3339DateTime | None]
    hide_date_range_on_invoice: NotRequired[bool]
    allow_fractional_quantities: NotRequired[bool]
    item_category: NotRequired[ItemCategoryOrStr | None]
    use_site_exchange_rate: NotRequired[bool | None]
    accounting_code: NotRequired[str | None]
    event_based_billing_metric_id: NotRequired[int]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr | None]
    unspsc_code: NotRequired[str | None]
    features: NotRequired[list[FeatureCatalogItemDict] | None]
    used_by: NotRequired[WalletProductUsageCountDict]
    price_point_summary: NotRequired[WalletProductPricePointSummaryDict]
