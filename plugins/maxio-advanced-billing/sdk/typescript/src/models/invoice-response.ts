import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type InvoiceResponse = {
  invoice: Invoice;
};

export const invoiceResponseSchema: Schema<InvoiceResponse> = s.object<InvoiceResponse>({
  invoice: invoiceSchema,
});
