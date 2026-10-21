from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .feature_catalog_item import FeatureCatalogItem, FeatureCatalogItemDict
from .product_family import ProductFamily, ProductFamilyDict
from .public_signup_page import PublicSignupPage, PublicSignupPageDict


class Product(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    """The product name"""

    handle: OptionalNullable[str] = UNSET
    """The product API handle"""

    description: OptionalNullable[str] = UNSET
    """The product description"""

    accounting_code: OptionalNullable[str] = UNSET
    """E.g., Internal ID or SKU Number"""

    request_credit_card: Optional[bool] = UNSET
    """Deprecated value that can be ignored unless you have legacy hosted pages. For Public Signup Page users, read this
    attribute from under the signup page."""

    expiration_interval: OptionalNullable[int] = UNSET
    """A numerical interval for the length a subscription to this product will run before it expires. See the
    description of interval for a description of how this value is coupled with an interval unit to calculate the full
    interval."""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    """A string representing the expiration interval unit for this product, either month, day or never"""

    created_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when this product was created"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp indicating when this product was last updated"""

    price_in_cents: Optional[int] = UNSET
    """The product price, in integer cents"""

    interval: Optional[int] = UNSET
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this product
    would renew every 30 days."""

    interval_unit: Optional[IntervalUnitOrStr] = UNSET
    """A string representing the interval unit for this product, either month or day"""

    initial_charge_in_cents: OptionalNullable[int] = UNSET
    """The up front charge you have specified."""

    trial_price_in_cents: OptionalNullable[int] = UNSET
    """The price of the trial period for a subscription to this product, in integer cents."""

    trial_interval: OptionalNullable[int] = UNSET
    """A numerical interval for the length of the trial period of a subscription to this product. See the description of
    interval for a description of how this value is coupled with an interval unit to calculate the full interval."""

    trial_interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the trial interval unit for this product, either month or day"""

    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp indicating when this product was archived"""

    require_credit_card: Optional[bool] = UNSET
    """Boolean that controls whether a payment profile is required to be entered for customers wishing to sign up on
    this product."""

    return_params: OptionalNullable[str] = UNSET
    taxable: Optional[bool] = UNSET
    update_return_url: OptionalNullable[str] = UNSET
    """The url to which a customer will be returned after a successful account update"""

    initial_charge_after_trial: OptionalNullable[bool] = UNSET
    version_number: Optional[int] = UNSET
    """The version of the product"""

    update_return_params: OptionalNullable[str] = UNSET
    """The parameters will append to the url after a successful account update. See `help documentation
    <https://help.chargify.com/products/product-editing.html#return-parameters-after-account-update>`__."""

    product_family: Optional[ProductFamily] = UNSET
    public_signup_pages: Optional[list[PublicSignupPage]] = UNSET
    product_price_point_name: Optional[str] = UNSET
    request_billing_address: Optional[bool] = UNSET
    """A boolean indicating whether to request a billing address on any Self-Service Pages that are used by subscribers
    of this product."""

    require_billing_address: Optional[bool] = UNSET
    """A boolean indicating whether a billing address is required to add a payment profile, especially at signup."""

    require_shipping_address: Optional[bool] = UNSET
    """A boolean indicating whether a shipping address is required for the customer, especially at signup."""

    tax_code: OptionalNullable[str] = UNSET
    """A string representing the tax code related to the product type. This is especially important when using AvaTax to
    tax based on locale. This attribute has a max length of 25 characters."""

    default_product_price_point_id: Optional[int] = UNSET
    use_site_exchange_rate: OptionalNullable[bool] = UNSET
    item_category: OptionalNullable[str] = UNSET
    """One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other"""

    product_price_point_id: Optional[int] = UNSET
    product_price_point_handle: OptionalNullable[str] = UNSET
    unspsc_code: OptionalNullable[str] = UNSET
    """(Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is sent as the
    commodity code on invoice line items for this product instead of the default derived from item_category."""

    features: OptionalNullable[list[FeatureCatalogItem]] = UNSET
    """The active feature catalog items attached to this product. Present only when the request includes
    ``include_features=true``."""


class ProductDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    handle: NotRequired[str | None]
    description: NotRequired[str | None]
    accounting_code: NotRequired[str | None]
    request_credit_card: NotRequired[bool]
    expiration_interval: NotRequired[int | None]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    price_in_cents: NotRequired[int]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr]
    initial_charge_in_cents: NotRequired[int | None]
    trial_price_in_cents: NotRequired[int | None]
    trial_interval: NotRequired[int | None]
    trial_interval_unit: NotRequired[IntervalUnitOrStr | None]
    archived_at: NotRequired[RFC3339DateTime | None]
    require_credit_card: NotRequired[bool]
    return_params: NotRequired[str | None]
    taxable: NotRequired[bool]
    update_return_url: NotRequired[str | None]
    initial_charge_after_trial: NotRequired[bool | None]
    version_number: NotRequired[int]
    update_return_params: NotRequired[str | None]
    product_family: NotRequired[ProductFamilyDict]
    public_signup_pages: NotRequired[list[PublicSignupPageDict]]
    product_price_point_name: NotRequired[str]
    request_billing_address: NotRequired[bool]
    require_billing_address: NotRequired[bool]
    require_shipping_address: NotRequired[bool]
    tax_code: NotRequired[str | None]
    default_product_price_point_id: NotRequired[int]
    use_site_exchange_rate: NotRequired[bool | None]
    item_category: NotRequired[str | None]
    product_price_point_id: NotRequired[int]
    product_price_point_handle: NotRequired[str | None]
    unspsc_code: NotRequired[str | None]
    features: NotRequired[list[FeatureCatalogItemDict] | None]
