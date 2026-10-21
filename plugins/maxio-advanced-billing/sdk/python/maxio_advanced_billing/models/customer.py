from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.entity_identifier_kind import EntityIdentifierKindOrStr


class Customer(SdkBaseModel):
    first_name: Optional[str] = UNSET
    """The first name of the customer"""

    last_name: Optional[str] = UNSET
    """The last name of the customer"""

    email: Optional[str] = UNSET
    """The email address of the customer"""

    cc_emails: OptionalNullable[str] = UNSET
    """“A comma-separated list of emails that should be cc’d on all customer communications (e.g., “joe@example.com,
    sue@example.com”)”"""

    organization: OptionalNullable[str] = UNSET
    """The organization of the customer. If no value, ``null`` or empty string is provided, ``organization`` will be
    populated with the customer's first and last name, separated with a space."""

    reference: OptionalNullable[str] = UNSET
    """The unique identifier used within your own application for this customer"""

    id: Optional[int] = UNSET
    """The customer ID in Chargify"""

    created_at: Optional[RFC3339DateTime] = UNSET
    """The timestamp in which the customer object was created in Chargify"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """The timestamp in which the customer object was last edited"""

    address: OptionalNullable[str] = UNSET
    """The customer’s shipping street address (e.g., “123 Main St.”)"""

    address_2: OptionalNullable[str] = UNSET
    """Second line of the customer’s shipping address e.g., “Apt. 100”"""

    city: OptionalNullable[str] = UNSET
    """The customer’s shipping address city (e.g., “Boston”)"""

    state: OptionalNullable[str] = UNSET
    """The customer’s shipping address state (e.g., “MA”)"""

    state_name: OptionalNullable[str] = UNSET
    """The customer's full name of state"""

    zip: OptionalNullable[str] = UNSET
    """The customer’s shipping address zip code (e.g., “12345”)"""

    country: OptionalNullable[str] = UNSET
    """The customer shipping address country"""

    country_name: OptionalNullable[str] = UNSET
    """The customer's full name of country"""

    phone: OptionalNullable[str] = UNSET
    """The phone number of the customer"""

    verified: OptionalNullable[bool] = UNSET
    """Is the customer verified to use ACH as a payment method."""

    portal_customer_created_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp of when the Billing Portal entry was created at for the customer"""

    portal_invite_last_sent_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp of when the Billing Portal invite was last sent at"""

    portal_invite_last_accepted_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp of when the Billing Portal invite was last accepted"""

    tax_exempt: Optional[bool] = UNSET
    """The tax exempt status for the customer. Acceptable values are true or 1 for true and false or 0 for false."""

    surcharging: Optional[bool] = UNSET
    """Whether surcharging is enabled for the customer. Only included on sites where surcharging control is enabled."""

    vat_number: OptionalNullable[str] = UNSET
    """The VAT business identification number for the customer. This number is used to determine VAT tax opt out rules.
    It is not validated when added or updated on a customer record. Instead, it is validated via VIES before calculating
    taxes. Only valid business identification numbers will allow for VAT opt out. When the customer holds an entity
    identifier, this field returns that identifier's value, whatever its kind."""

    vat_country: OptionalNullable[str] = UNSET
    """The two-letter ISO 3166-1 country code that qualifies the customer's VAT number. Set to ``null`` when an
    identifier is stored through ``entity_identifier_kind`` for a kind that is not tied to a VAT country, meaning
    ``company_reg``, ``gln``, ``duns``, or ``lei``."""

    entity_identifier_kind: OptionalNullable[EntityIdentifierKindOrStr] = UNSET
    """The kind of tax or business identifier held by the customer. Returned as ``null`` when the customer has no entity
    identifier, including a legacy customer whose ``vat_number`` predates entity identifiers."""

    entity_identifier_value: OptionalNullable[str] = UNSET
    """The value of the customer's tax or business identifier. Returned as ``null`` when the customer has no entity
    identifier."""

    parent_id: OptionalNullable[int] = UNSET
    """The parent ID in Chargify if applicable. Parent is another Customer object."""

    locale: OptionalNullable[str] = UNSET
    """The locale for the customer to identify language-region"""

    default_subscription_group_uid: OptionalNullable[str] = UNSET
    salesforce_id: OptionalNullable[str] = UNSET
    """The Salesforce ID for the customer"""

    tax_exempt_reason: OptionalNullable[str] = UNSET
    """The Tax Exemption Reason Code for the customer"""

    default_auto_renewal_profile_id: OptionalNullable[int] = UNSET
    """The default auto-renewal profile ID for the customer"""

    maxioid: OptionalNullable[str] = UNSET
    """The Maxio-generated unique identifier for the customer."""

    branding_theme_id: OptionalNullable[int] = UNSET
    """The ID of the Branding Theme assigned to this customer as the customer's default Branding Theme. This
    customer-level Branding Theme is used when a subscription does not have its own subscription-level Branding Theme.
    Available only when Branding Themes are enabled for the site."""


class CustomerDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    cc_emails: NotRequired[str | None]
    organization: NotRequired[str | None]
    reference: NotRequired[str | None]
    id: NotRequired[int]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    address: NotRequired[str | None]
    address_2: NotRequired[str | None]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    state_name: NotRequired[str | None]
    zip: NotRequired[str | None]
    country: NotRequired[str | None]
    country_name: NotRequired[str | None]
    phone: NotRequired[str | None]
    verified: NotRequired[bool | None]
    portal_customer_created_at: NotRequired[RFC3339DateTime | None]
    portal_invite_last_sent_at: NotRequired[RFC3339DateTime | None]
    portal_invite_last_accepted_at: NotRequired[RFC3339DateTime | None]
    tax_exempt: NotRequired[bool]
    surcharging: NotRequired[bool]
    vat_number: NotRequired[str | None]
    vat_country: NotRequired[str | None]
    entity_identifier_kind: NotRequired[EntityIdentifierKindOrStr | None]
    entity_identifier_value: NotRequired[str | None]
    parent_id: NotRequired[int | None]
    locale: NotRequired[str | None]
    default_subscription_group_uid: NotRequired[str | None]
    salesforce_id: NotRequired[str | None]
    tax_exempt_reason: NotRequired[str | None]
    default_auto_renewal_profile_id: NotRequired[int | None]
    maxioid: NotRequired[str | None]
    branding_theme_id: NotRequired[int | None]
