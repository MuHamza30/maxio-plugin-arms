import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoicePayerChangeSchema, type InvoicePayerChange } from "./invoice-payer-change.js";

export type CustomerPayerChange = {
  before: InvoicePayerChange;
  after: InvoicePayerChange;
};

export const customerPayerChangeSchema: Schema<CustomerPayerChange> = s.object<CustomerPayerChange>({
  before: invoicePayerChangeSchema,
  after: invoicePayerChangeSchema,
});
