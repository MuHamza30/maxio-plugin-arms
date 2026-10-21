import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoiceTaxBreakout = {
  uid?: string;
  taxableAmount?: string;
  taxAmount?: string;
  taxExemptAmount?: string;
};

export const invoiceTaxBreakoutSchema: Schema<InvoiceTaxBreakout> = s.object<InvoiceTaxBreakout>({
  uid: s.optional(s.string()),
  taxableAmount: s.optional(s.string()),
  taxAmount: s.optional(s.string()),
  taxExemptAmount: s.optional(s.string()),
  _keysMap: {
    taxableAmount: "taxable_amount",
    taxAmount: "tax_amount",
    taxExemptAmount: "tax_exempt_amount",
  },
});
