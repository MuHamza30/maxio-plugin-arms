import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PayerAttributes = {
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
  locale?: string;
  vatNumber?: string;
  taxExempt?: boolean;
  taxExemptReason?: string;
  /**
   * (Optional) A set of key/value pairs representing custom fields and their values. Metafields
   * will be created “on-the-fly” in your site for a given key, if they have not been created yet.
   */
  metafields?: Record<string, string>;
};

export const payerAttributesSchema: Schema<PayerAttributes> = s.object<PayerAttributes>({
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
  taxExempt: s.optional(s.boolean()),
  taxExemptReason: s.optional(s.string()),
  metafields: s.optional(s.record(s.string(), s.string())),
  _keysMap: {
    firstName: "first_name",
    lastName: "last_name",
    ccEmails: "cc_emails",
    address2: "address_2",
    vatNumber: "vat_number",
    taxExempt: "tax_exempt",
    taxExemptReason: "tax_exempt_reason",
  },
});
