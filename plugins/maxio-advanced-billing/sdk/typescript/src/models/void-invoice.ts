import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type VoidInvoice = {
  reason: string;
};

export const voidInvoiceSchema: Schema<VoidInvoice> = s.object<VoidInvoice>({
  reason: s.string(),
});
