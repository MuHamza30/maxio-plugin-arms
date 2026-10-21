import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Overrides the default address. */
export type CreateInvoiceAddress = {
  firstName?: string;
  lastName?: string;
  phone?: string;
  address?: string;
  address2?: string;
  city?: string;
  state?: string;
  zip?: string;
  country?: string;
};

export const createInvoiceAddressSchema: Schema<CreateInvoiceAddress> = s.object<CreateInvoiceAddress>({
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  phone: s.optional(s.string()),
  address: s.optional(s.string()),
  address2: s.optional(s.string()),
  city: s.optional(s.string()),
  state: s.optional(s.string()),
  zip: s.optional(s.string()),
  country: s.optional(s.string()),
  _keysMap: {
    firstName: "first_name",
    lastName: "last_name",
    address2: "address_2",
  },
});
