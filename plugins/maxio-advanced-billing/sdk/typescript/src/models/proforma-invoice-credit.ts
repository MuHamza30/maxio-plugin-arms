import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ProformaInvoiceCredit = {
  uid?: string;
  memo?: string;
  originalAmount?: string;
  appliedAmount?: string;
};

export const proformaInvoiceCreditSchema: Schema<ProformaInvoiceCredit> = s.object<ProformaInvoiceCredit>({
  uid: s.optional(s.string()),
  memo: s.optional(s.string()),
  originalAmount: s.optional(s.string()),
  appliedAmount: s.optional(s.string()),
  _keysMap: {
    originalAmount: "original_amount",
    appliedAmount: "applied_amount",
  },
});
