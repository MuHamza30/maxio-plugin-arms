import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceAddressSchema, type InvoiceAddress } from "./invoice-address.js";

/** Information about the seller (merchant) listed on the masthead of the invoice. */
export type InvoiceSeller = {
  name?: string;
  address?: InvoiceAddress;
  phone?: string;
  logoUrl?: string | null;
};

export const invoiceSellerSchema: Schema<InvoiceSeller> = s.object<InvoiceSeller>({
  name: s.optional(s.string()),
  address: s.optional(s.lazy(() => invoiceAddressSchema)),
  phone: s.optional(s.string()),
  logoUrl: s.optionalNullable(s.string()),
  _keysMap: {
    logoUrl: "logo_url",
  },
});
