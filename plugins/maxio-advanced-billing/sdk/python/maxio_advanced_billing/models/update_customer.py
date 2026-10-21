from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.entity_identifier_kind import EntityIdentifierKindOrStr


class UpdateCustomer(SdkBaseModel):
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    email: Optional[str] = UNSET
    cc_emails: Optional[str] = UNSET
    organization: Optional[str] = UNSET
    reference: Optional[str] = UNSET
    address: Optional[str] = UNSET
    address_2: Optional[str] = UNSET
    city: Optional[str] = UNSET
    state: Optional[str] = UNSET
    zip: Optional[str] = UNSET
    country: Optional[str] = UNSET
    phone: Optional[str] = UNSET
    locale: Optional[str] = UNSET
    """Set a specific language on a customer record."""

    vat_number: Optional[str] = UNSET
    vat_country: Optional[str] = UNSET
    """The two-letter ISO 3166-1 country code that qualifies the customer's tax ID. Required when
    ``entity_identifier_kind`` is ``vat_eu`` or ``national_tax``, and used to derive the kind when only the legacy
    ``vat_number`` is sent."""

    entity_identifier_kind: Optional[EntityIdentifierKindOrStr] = UNSET
    """The kind of tax or business identifier held by the customer:
    - ``vat_eu``: an EU VAT number. Requires ``vat_country`` to be an EU member state code or ``GB``.
    - ``national_tax``: a national tax ID registered outside the EU. Requires ``vat_country`` to be one of ``AL``,
        ``AM``, ``AR``, ``AU``, ``BR``, ``CA``, ``CH``, ``DZ``, ``IN``, ``MX``, ``NO``, ``NZ``, or ``ZA``.
    - ``company_reg``: a company registration number, such as a French SIREN. No ``vat_country`` is required.
    - ``gln``: a Global Location Number. The value must be 13 digits.
    - ``duns``: a D-U-N-S Number. The value must be 9 digits.
    - ``lei``: a Legal Entity Identifier. The value must be 20 characters: 18 letters or digits followed by 2 digits.

    A customer holds one identifier at a time. Saving an identifier of a different kind replaces the existing one."""

    entity_identifier_value: Optional[str] = UNSET
    """The customer's tax or business identifier, sent together with ``entity_identifier_kind``. Advanced Billing trims
    surrounding whitespace and stores the value in uppercase."""

    tax_exempt: Optional[bool] = UNSET
    surcharging: Optional[bool] = UNSET
    """Whether surcharging is enabled for the customer. Only applied on sites where surcharging control is enabled."""

    tax_exempt_reason: Optional[str] = UNSET
    parent_id: OptionalNullable[int] = UNSET
    verified: OptionalNullable[bool] = UNSET
    """Is the customer verified to use ACH as a payment method. Available only on the Authorize.Net gateway."""

    salesforce_id: OptionalNullable[str] = UNSET
    """The Salesforce ID of the customer"""

    branding_theme_id: OptionalNullable[int] = UNSET
    """The ID of the Branding Theme assigned to this customer as the customer's default Branding Theme. This
    customer-level Branding Theme is used when a subscription does not have its own subscription-level Branding Theme.
    Available only when Branding Themes are enabled for the site."""


class UpdateCustomerDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    cc_emails: NotRequired[str]
    organization: NotRequired[str]
    reference: NotRequired[str]
    address: NotRequired[str]
    address_2: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]
    vat_number: NotRequired[str]
    vat_country: NotRequired[str]
    entity_identifier_kind: NotRequired[EntityIdentifierKindOrStr]
    entity_identifier_value: NotRequired[str]
    tax_exempt: NotRequired[bool]
    surcharging: NotRequired[bool]
    tax_exempt_reason: NotRequired[str]
    parent_id: NotRequired[int | None]
    verified: NotRequired[bool | None]
    salesforce_id: NotRequired[str | None]
    branding_theme_id: NotRequired[int | None]
