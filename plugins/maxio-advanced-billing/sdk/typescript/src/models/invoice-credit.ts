import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoiceCredit = {
  uid?: string;
  creditNoteNumber?: string;
  creditNoteUid?: string;
  transactionTime?: Date;
  memo?: string;
  originalAmount?: string;
  appliedAmount?: string;
};

export const invoiceCreditSchema: Schema<InvoiceCredit> = s.object<InvoiceCredit>({
  uid: s.optional(s.string()),
  creditNoteNumber: s.optional(s.string()),
  creditNoteUid: s.optional(s.string()),
  transactionTime: s.optional(s.dateTime()),
  memo: s.optional(s.string()),
  originalAmount: s.optional(s.string()),
  appliedAmount: s.optional(s.string()),
  _keysMap: {
    creditNoteNumber: "credit_note_number",
    creditNoteUid: "credit_note_uid",
    transactionTime: "transaction_time",
    originalAmount: "original_amount",
    appliedAmount: "applied_amount",
  },
});
