import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreditNoteApplication = {
  uid?: string;
  transactionTime?: Date;
  invoiceUid?: string;
  memo?: string;
  appliedAmount?: string;
};

export const creditNoteApplicationSchema: Schema<CreditNoteApplication> = s.object<CreditNoteApplication>({
  uid: s.optional(s.string()),
  transactionTime: s.optional(s.dateTime()),
  invoiceUid: s.optional(s.string()),
  memo: s.optional(s.string()),
  appliedAmount: s.optional(s.string()),
  _keysMap: {
    transactionTime: "transaction_time",
    invoiceUid: "invoice_uid",
    appliedAmount: "applied_amount",
  },
});
