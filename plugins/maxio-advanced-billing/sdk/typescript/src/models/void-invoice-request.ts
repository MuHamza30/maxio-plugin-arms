import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { voidInvoiceSchema, type VoidInvoice } from "./void-invoice.js";

export type VoidInvoiceRequest = {
  void: VoidInvoice;
};

export const voidInvoiceRequestSchema: Schema<VoidInvoiceRequest> = s.object<VoidInvoiceRequest>({
  void: voidInvoiceSchema,
});
