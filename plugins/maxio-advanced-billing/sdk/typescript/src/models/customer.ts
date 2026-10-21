import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { entityIdentifierKindSchema, type EntityIdentifierKind } from "./entity-identifier-kind.js";

export type Customer = {
  /** The first name of the customer */
  firstName?: string;
  /** The last name of the customer */
  lastName?: string;
  /** The email address of the customer */
  email?: string;
  /**
   * “A comma-separated list of emails that should be cc’d on all customer communications (e.g.,
   * “joe@example.com, sue@example.com”)”
   */
  ccEmails?: string | null;
  /**
   * The organization of the customer. If no value, `null` or empty string is provided,
   * `organization` will be populated with the customer's first and last name, separated with a
   * space.
   */
  organization?: string | null;
  /** The unique identifier used within your own application for this customer */
  reference?: string | null;
  /** The customer ID in Chargify */
  id?: number;
  /** The timestamp in which the customer object was created in Chargify */
  createdAt?: Date;
  /** The timestamp in which the customer object was last edited */
  updatedAt?: Date;
  /** The customer’s shipping street address (e.g., “123 Main St.”) */
  address?: string | null;
  /** Second line of the customer’s shipping address e.g., “Apt. 100” */
  address2?: string | null;
  /** The customer’s shipping address city (e.g., “Boston”) */
  city?: string | null;
  /** The customer’s shipping address state (e.g., “MA”) */
  state?: string | null;
  /** The customer's full name of state */
  stateName?: string | null;
  /** The customer’s shipping address zip code (e.g., “12345”) */
  zip?: string | null;
  /** The customer shipping address country */
  country?: string | null;
  /** The customer's full name of country */
  countryName?: string | null;
  /** The phone number of the customer */
  phone?: string | null;
  /** Is the customer verified to use ACH as a payment method. */
  verified?: boolean | null;
  /** The timestamp of when the Billing Portal entry was created at for the customer */
  portalCustomerCreatedAt?: Date | null;
  /** The timestamp of when the Billing Portal invite was last sent at */
  portalInviteLastSentAt?: Date | null;
  /** The timestamp of when the Billing Portal invite was last accepted */
  portalInviteLastAcceptedAt?: Date | null;
  /**
   * The tax exempt status for the customer. Acceptable values are true or 1 for true and false or 0
   * for false.
   */
  taxExempt?: boolean;
  /**
   * Whether surcharging is enabled for the customer. Only included on sites where surcharging
   * control is enabled.
   */
  surcharging?: boolean;
  /**
   * The VAT business identification number for the customer. This number is used to determine VAT
   * tax opt out rules. It is not validated when added or updated on a customer record. Instead, it
   * is validated via VIES before calculating taxes. Only valid business identification numbers will
   * allow for VAT opt out. When the customer holds an entity identifier, this field returns that
   * identifier's value, whatever its kind.
   */
  vatNumber?: string | null;
  /**
   * The two-letter ISO 3166-1 country code that qualifies the customer's VAT number. Set to `null`
   * when an identifier is stored through `entity_identifier_kind` for a kind that is not tied to a
   * VAT country, meaning `company_reg`, `gln`, `duns`, or `lei`.
   */
  vatCountry?: string | null;
  /**
   * The kind of tax or business identifier held by the customer. Returned as `null` when the
   * customer has no entity identifier, including a legacy customer whose `vat_number` predates
   * entity identifiers.
   */
  entityIdentifierKind?: EntityIdentifierKind | null;
  /**
   * The value of the customer's tax or business identifier. Returned as `null` when the customer
   * has no entity identifier.
   */
  entityIdentifierValue?: string | null;
  /** The parent ID in Chargify if applicable. Parent is another Customer object. */
  parentId?: number | null;
  /** The locale for the customer to identify language-region */
  locale?: string | null;
  defaultSubscriptionGroupUid?: string | null;
  /** The Salesforce ID for the customer */
  salesforceId?: string | null;
  /** The Tax Exemption Reason Code for the customer */
  taxExemptReason?: string | null;
  /** The default auto-renewal profile ID for the customer */
  defaultAutoRenewalProfileId?: number | null;
  /** The Maxio-generated unique identifier for the customer. */
  maxioid?: string | null;
  /**
   * The ID of the Branding Theme assigned to this customer as the customer's default Branding
   * Theme. This customer-level Branding Theme is used when a subscription does not have its own
   * subscription-level Branding Theme. Available only when Branding Themes are enabled for the
   * site.
   */
  brandingThemeId?: number | null;
};

export const customerSchema: Schema<Customer> = s.object<Customer>({
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  email: s.optional(s.string()),
  ccEmails: s.optionalNullable(s.string()),
  organization: s.optionalNullable(s.string()),
  reference: s.optionalNullable(s.string()),
  id: s.optional(s.int()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  address: s.optionalNullable(s.string()),
  address2: s.optionalNullable(s.string()),
  city: s.optionalNullable(s.string()),
  state: s.optionalNullable(s.string()),
  stateName: s.optionalNullable(s.string()),
  zip: s.optionalNullable(s.string()),
  country: s.optionalNullable(s.string()),
  countryName: s.optionalNullable(s.string()),
  phone: s.optionalNullable(s.string()),
  verified: s.optionalNullable(s.boolean()),
  portalCustomerCreatedAt: s.optionalNullable(s.dateTime()),
  portalInviteLastSentAt: s.optionalNullable(s.dateTime()),
  portalInviteLastAcceptedAt: s.optionalNullable(s.dateTime()),
  taxExempt: s.optional(s.boolean()),
  surcharging: s.optional(s.boolean()),
  vatNumber: s.optionalNullable(s.string()),
  vatCountry: s.optionalNullable(s.string()),
  entityIdentifierKind: s.optionalNullable(s.lazy(() => entityIdentifierKindSchema)),
  entityIdentifierValue: s.optionalNullable(s.string()),
  parentId: s.optionalNullable(s.int()),
  locale: s.optionalNullable(s.string()),
  defaultSubscriptionGroupUid: s.optionalNullable(s.string()),
  salesforceId: s.optionalNullable(s.string()),
  taxExemptReason: s.optionalNullable(s.string()),
  defaultAutoRenewalProfileId: s.optionalNullable(s.int()),
  maxioid: s.optionalNullable(s.string()),
  brandingThemeId: s.optionalNullable(s.int()),
  _keysMap: {
    firstName: "first_name",
    lastName: "last_name",
    ccEmails: "cc_emails",
    createdAt: "created_at",
    updatedAt: "updated_at",
    address2: "address_2",
    stateName: "state_name",
    countryName: "country_name",
    portalCustomerCreatedAt: "portal_customer_created_at",
    portalInviteLastSentAt: "portal_invite_last_sent_at",
    portalInviteLastAcceptedAt: "portal_invite_last_accepted_at",
    taxExempt: "tax_exempt",
    vatNumber: "vat_number",
    vatCountry: "vat_country",
    entityIdentifierKind: "entity_identifier_kind",
    entityIdentifierValue: "entity_identifier_value",
    parentId: "parent_id",
    defaultSubscriptionGroupUid: "default_subscription_group_uid",
    salesforceId: "salesforce_id",
    taxExemptReason: "tax_exempt_reason",
    defaultAutoRenewalProfileId: "default_auto_renewal_profile_id",
    brandingThemeId: "branding_theme_id",
  },
});
