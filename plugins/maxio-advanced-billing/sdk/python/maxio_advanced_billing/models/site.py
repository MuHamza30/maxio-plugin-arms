from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .allocation_settings import AllocationSettings, AllocationSettingsDict
from .net_terms import NetTerms, NetTermsDict
from .organization_address import OrganizationAddress, OrganizationAddressDict
from .tax_configuration import TaxConfiguration, TaxConfigurationDict


class Site(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    subdomain: Optional[str] = UNSET
    currency: Optional[str] = UNSET
    seller_id: Optional[int] = UNSET
    non_primary_currencies: Optional[list[str]] = UNSET
    relationship_invoicing_enabled: Optional[bool] = UNSET
    schedule_subscription_cancellation_enabled: Optional[bool] = UNSET
    customer_hierarchy_enabled: Optional[bool] = UNSET
    whopays_enabled: Optional[bool] = UNSET
    whopays_default_payer: Optional[str] = UNSET
    allocation_settings: Optional[AllocationSettings] = UNSET
    default_payment_collection_method: Optional[str] = UNSET
    organization_address: Optional[OrganizationAddress] = UNSET
    tax_configuration: Optional[TaxConfiguration] = UNSET
    net_terms: Optional[NetTerms] = UNSET
    multi_frequency_enabled: Optional[bool] = UNSET
    """Whether the site has the multi-frequency billing feature enabled. Only present when relationship invoicing is
    active."""

    auto_renewals_enabled: Optional[bool] = UNSET
    """Whether the auto-renewals feature is enabled for this site."""

    portal_enabled: Optional[bool] = UNSET
    """Whether the Billing Portal is enabled for this site."""

    test: Optional[bool] = UNSET


class SiteDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    subdomain: NotRequired[str]
    currency: NotRequired[str]
    seller_id: NotRequired[int]
    non_primary_currencies: NotRequired[list[str]]
    relationship_invoicing_enabled: NotRequired[bool]
    schedule_subscription_cancellation_enabled: NotRequired[bool]
    customer_hierarchy_enabled: NotRequired[bool]
    whopays_enabled: NotRequired[bool]
    whopays_default_payer: NotRequired[str]
    allocation_settings: NotRequired[AllocationSettingsDict]
    default_payment_collection_method: NotRequired[str]
    organization_address: NotRequired[OrganizationAddressDict]
    tax_configuration: NotRequired[TaxConfigurationDict]
    net_terms: NotRequired[NetTermsDict]
    multi_frequency_enabled: NotRequired[bool]
    auto_renewals_enabled: NotRequired[bool]
    portal_enabled: NotRequired[bool]
    test: NotRequired[bool]
