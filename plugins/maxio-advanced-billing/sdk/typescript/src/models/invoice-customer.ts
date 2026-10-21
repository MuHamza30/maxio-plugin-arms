import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Information about the customer who is owner or recipient of the invoiced subscription. */
export type InvoiceCustomer = {
  chargifyId?: number | null;
  firstName?: string;
  lastName?: string;
  organization?: string | null;
  email?: string;
  vatNumber?: string | null;
  reference?: string | null;
};

export const invoiceCustomerSchema: Schema<InvoiceCustomer> = s.object<InvoiceCustomer>({
  chargifyId: s.optionalNullable(s.int()),
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  organization: s.optionalNullable(s.string()),
  email: s.optional(s.string()),
  vatNumber: s.optionalNullable(s.string()),
  reference: s.optionalNullable(s.string()),
  _keysMap: {
    chargifyId: "chargify_id",
    firstName: "first_name",
    lastName: "last_name",
    vatNumber: "vat_number",
  },
});
