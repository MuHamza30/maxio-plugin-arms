import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoicePayerChange = {
  firstName?: string;
  lastName?: string;
  organization?: string;
  email?: string;
};

export const invoicePayerChangeSchema: Schema<InvoicePayerChange> = s.object<InvoicePayerChange>({
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  organization: s.optional(s.string()),
  email: s.optional(s.string()),
  _keysMap: {
    firstName: "first_name",
    lastName: "last_name",
  },
});
