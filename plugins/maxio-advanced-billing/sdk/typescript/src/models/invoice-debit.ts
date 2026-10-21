import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { debitNoteRoleSchema, type DebitNoteRole } from "./debit-note-role.js";

export type InvoiceDebit = {
  uid?: string;
  debitNoteNumber?: string;
  debitNoteUid?: string;
  /** The role of the debit note. */
  role?: DebitNoteRole;
  transactionTime?: Date;
  memo?: string;
  originalAmount?: string;
  appliedAmount?: string;
};

export const invoiceDebitSchema: Schema<InvoiceDebit> = s.object<InvoiceDebit>({
  uid: s.optional(s.string()),
  debitNoteNumber: s.optional(s.string()),
  debitNoteUid: s.optional(s.string()),
  role: s.optional(s.lazy(() => debitNoteRoleSchema)),
  transactionTime: s.optional(s.dateTime()),
  memo: s.optional(s.string()),
  originalAmount: s.optional(s.string()),
  appliedAmount: s.optional(s.string()),
  _keysMap: {
    debitNoteNumber: "debit_note_number",
    debitNoteUid: "debit_note_uid",
    transactionTime: "transaction_time",
    originalAmount: "original_amount",
    appliedAmount: "applied_amount",
  },
});
