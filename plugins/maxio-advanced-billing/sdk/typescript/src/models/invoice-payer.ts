import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoicePayer = {
  chargifyId?: number;
  firstName?: string;
  lastName?: string;
  organization?: string | null;
  email?: string;
  vatNumber?: string | null;
};

export const invoicePayerSchema: Schema<InvoicePayer> = s.object<InvoicePayer>({
  chargifyId: s.optional(s.int()),
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  organization: s.optionalNullable(s.string()),
  email: s.optional(s.string()),
  vatNumber: s.optionalNullable(s.string()),
  _keysMap: {
    chargifyId: "chargify_id",
    firstName: "first_name",
    lastName: "last_name",
    vatNumber: "vat_number",
  },
});
