import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createInvoiceSchema, type CreateInvoice } from "./create-invoice.js";

export type CreateInvoiceRequest = {
  invoice: CreateInvoice;
};

export const createInvoiceRequestSchema: Schema<CreateInvoiceRequest> = s.object<CreateInvoiceRequest>({
  invoice: createInvoiceSchema,
});
