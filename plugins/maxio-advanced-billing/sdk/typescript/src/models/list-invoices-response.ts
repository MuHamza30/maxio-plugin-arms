import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type ListInvoicesResponse = {
  invoices: Invoice[];
};

export const listInvoicesResponseSchema: Schema<ListInvoicesResponse> = s.object<ListInvoicesResponse>({
  invoices: s.array(s.lazy(() => invoiceSchema)),
});
