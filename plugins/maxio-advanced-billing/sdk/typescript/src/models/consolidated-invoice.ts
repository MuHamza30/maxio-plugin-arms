import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type ConsolidatedInvoice = {
  invoices?: Invoice[];
};

export const consolidatedInvoiceSchema: Schema<ConsolidatedInvoice> = s.object<ConsolidatedInvoice>({
  invoices: s.optional(s.array(s.lazy(() => invoiceSchema))),
});
