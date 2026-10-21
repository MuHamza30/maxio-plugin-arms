import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { entityIdentifierKindSchema, type EntityIdentifierKind } from "./entity-identifier-kind.js";

export type UpdateCustomer = {
  firstName?: string;
  lastName?: string;
  email?: string;
  ccEmails?: string;
  organization?: string;
  reference?: string;
  address?: string;
  address2?: string;
  city?: string;
  state?: string;
  zip?: string;
  country?: string;
  phone?: string;
  /** Set a specific language on a customer record. */
  locale?: string;
  vatNumber?: string;
  /**
   * The two-letter ISO 3166-1 country code that qualifies the customer's tax ID. Required when
   * `entity_identifier_kind` is `vat_eu` or `national_tax`, and used to derive the kind when only
   * the legacy `vat_number` is sent.
   */
  vatCountry?: string;
  /**
   * The kind of tax or business identifier held by the customer:
   * - `vat_eu`: an EU VAT number. Requires `vat_country` to be an EU member state code or `GB`.
   * - `national_tax`: a national tax ID registered outside the EU. Requires `vat_country` to be one
   *   of `AL`, `AM`, `AR`, `AU`, `BR`, `CA`, `CH`, `DZ`, `IN`, `MX`, `NO`, `NZ`, or `ZA`.
   * - `company_reg`: a company registration number, such as a French SIREN. No `vat_country` is
   *   required.
   * - `gln`: a Global Location Number. The value must be 13 digits.
   * - `duns`: a D-U-N-S Number. The value must be 9 digits.
   * - `lei`: a Legal Entity Identifier. The value must be 20 characters: 18 letters or digits
   *   followed by 2 digits.
   *
   * A customer holds one identifier at a time. Saving an identifier of a different kind replaces
   * the existing one.
   */
  entityIdentifierKind?: EntityIdentifierKind;
  /**
   * The customer's tax or business identifier, sent together with `entity_identifier_kind`.
   * Advanced Billing trims surrounding whitespace and stores the value in uppercase.
   */
  entityIdentifierValue?: string;
  taxExempt?: boolean;
  /**
   * Whether surcharging is enabled for the customer. Only applied on sites where surcharging
   * control is enabled.
   */
  surcharging?: boolean;
  taxExemptReason?: string;
  parentId?: number | null;
  /**
   * Is the customer verified to use ACH as a payment method. Available only on the Authorize.Net
   * gateway.
   */
  verified?: boolean | null;
  /** The Salesforce ID of the customer */
  salesforceId?: string | null;
  /**
   * The ID of the Branding Theme assigned to this customer as the customer's default Branding
   * Theme. This customer-level Branding Theme is used when a subscription does not have its own
   * subscription-level Branding Theme. Available only when Branding Themes are enabled for the
   * site.
   */
  brandingThemeId?: number | null;
};

export const updateCustomerSchema: Schema<UpdateCustomer> = s.object<UpdateCustomer>({
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  email: s.optional(s.string()),
  ccEmails: s.optional(s.string()),
  organization: s.optional(s.string()),
  reference: s.optional(s.string()),
  address: s.optional(s.string()),
  address2: s.optional(s.string()),
  city: s.optional(s.string()),
  state: s.optional(s.string()),
  zip: s.optional(s.string()),
  country: s.optional(s.string()),
  phone: s.optional(s.string()),
  locale: s.optional(s.string()),
  vatNumber: s.optional(s.string()),
  vatCountry: s.optional(s.string()),
  entityIdentifierKind: s.optional(s.lazy(() => entityIdentifierKindSchema)),
  entityIdentifierValue: s.optional(s.string()),
  taxExempt: s.optional(s.boolean()),
  surcharging: s.optional(s.boolean()),
  taxExemptReason: s.optional(s.string()),
  parentId: s.optionalNullable(s.int()),
  verified: s.optionalNullable(s.boolean()),
  salesforceId: s.optionalNullable(s.string()),
  brandingThemeId: s.optionalNullable(s.int()),
  _keysMap: {
    firstName: "first_name",
    lastName: "last_name",
    ccEmails: "cc_emails",
    address2: "address_2",
    vatNumber: "vat_number",
    vatCountry: "vat_country",
    entityIdentifierKind: "entity_identifier_kind",
    entityIdentifierValue: "entity_identifier_value",
    taxExempt: "tax_exempt",
    taxExemptReason: "tax_exempt_reason",
    parentId: "parent_id",
    salesforceId: "salesforce_id",
    brandingThemeId: "branding_theme_id",
  },
});
