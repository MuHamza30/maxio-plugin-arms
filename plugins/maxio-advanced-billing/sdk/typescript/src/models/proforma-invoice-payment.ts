import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ProformaInvoicePayment = {
  memo?: string;
  originalAmount?: string;
  appliedAmount?: string;
  prepayment?: boolean;
};

export const proformaInvoicePaymentSchema: Schema<ProformaInvoicePayment> = s.object<ProformaInvoicePayment>({
  memo: s.optional(s.string()),
  originalAmount: s.optional(s.string()),
  appliedAmount: s.optional(s.string()),
  prepayment: s.optional(s.boolean()),
  _keysMap: {
    originalAmount: "original_amount",
    appliedAmount: "applied_amount",
  },
});
