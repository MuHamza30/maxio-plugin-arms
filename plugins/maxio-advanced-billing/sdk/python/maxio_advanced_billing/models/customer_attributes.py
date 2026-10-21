from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CustomerAttributes(SdkBaseModel):
    first_name: Optional[str] = UNSET
    """The first name of the customer. Required when creating a customer via attributes."""

    last_name: Optional[str] = UNSET
    """The last name of the customer. Required when creating a customer via attributes."""

    email: Optional[str] = UNSET
    """The email address of the customer. Required when creating a customer via attributes."""

    cc_emails: Optional[str] = UNSET
    """(Optional) A list of emails that should be cc’d on all customer communications."""

    organization: Optional[str] = UNSET
    """(Optional) The organization/company of the customer."""

    reference: Optional[str] = UNSET
    """(Optional) A customer “reference”, or unique identifier from your app, stored in Chargify. Can be used so that
    you may reference your customer’s within Chargify using the same unique value you use in your application."""

    address: Optional[str] = UNSET
    """(Optional) The customer’s shipping street address (e.g., “123 Main St.”)."""

    address_2: OptionalNullable[str] = UNSET
    """(Optional) Second line of the customer’s shipping address e.g., “Apt. 100”"""

    city: Optional[str] = UNSET
    """(Optional) The customer’s shipping address city (e.g., “Boston”)."""

    state: Optional[str] = UNSET
    """“(Optional) The customer’s shipping address state (e.g., “MA”). This must conform to the `ISO_3166-1
    <https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ in order to be valid for tax locale purposes.”"""

    zip: Optional[str] = UNSET
    """(Optional) The customer’s shipping address zip code (e.g., “12345”)."""

    country: Optional[str] = UNSET
    """“(Optional) The customer shipping address country, required in `ISO_3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format (e.g., “US”).”"""

    phone: Optional[str] = UNSET
    """(Optional) The phone number of the customer."""

    verified: Optional[bool] = UNSET
    tax_exempt: Optional[bool] = UNSET
    """(Optional) The tax_exempt status of the customer. Acceptable values are true or 1 for true and false or 0 for
    false."""

    surcharging: Optional[bool] = UNSET
    """(Optional) Whether surcharging is enabled for the customer. Defaults to ``true`` when omitted. Only applied on
    sites where surcharging control is enabled."""

    vat_number: Optional[str] = UNSET
    """(Optional) Supplying the VAT number allows EU customers to opt-out of the Value Added Tax assuming the merchant
    address and customer billing address are not within the same EU country. It’s important to omit the country code
    from the VAT number upon entry. Otherwise, taxes will be assessed upon the purchase."""

    metafields: Optional[dict[str, str]] = UNSET
    """(Optional) A set of key/value pairs representing custom fields and their values. Metafields will be created
    “on-the-fly” in your site for a given key, if they have not been created yet."""

    parent_id: OptionalNullable[int] = UNSET
    """The parent ID in Chargify if applicable. Parent is another Customer object."""

    salesforce_id: OptionalNullable[str] = UNSET
    """(Optional) The Salesforce ID of the customer."""

    default_auto_renewal_profile_id: OptionalNullable[int] = UNSET
    """(Optional) The default auto-renewal profile ID for the customer"""


class CustomerAttributesDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    cc_emails: NotRequired[str]
    organization: NotRequired[str]
    reference: NotRequired[str]
    address: NotRequired[str]
    address_2: NotRequired[str | None]
    city: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    phone: NotRequired[str]
    verified: NotRequired[bool]
    tax_exempt: NotRequired[bool]
    surcharging: NotRequired[bool]
    vat_number: NotRequired[str]
    metafields: NotRequired[dict[str, str]]
    parent_id: NotRequired[int | None]
    salesforce_id: NotRequired[str | None]
    default_auto_renewal_profile_id: NotRequired[int | None]
