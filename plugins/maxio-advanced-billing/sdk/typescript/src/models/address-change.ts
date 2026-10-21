import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceAddressSchema, type InvoiceAddress } from "./invoice-address.js";

export type AddressChange = {
  before: InvoiceAddress;
  after: InvoiceAddress;
};

export const addressChangeSchema: Schema<AddressChange> = s.object<AddressChange>({
  before: invoiceAddressSchema,
  after: invoiceAddressSchema,
});
