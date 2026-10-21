import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { appliedCreditNoteDataSchema, type AppliedCreditNoteData } from "./applied-credit-note-data.js";

/** Example schema for an `apply_credit_note` event */
export type ApplyCreditNoteEventData = {
  /**
   * Unique identifier for the credit note application. It is generated automatically by Chargify
   * and has the prefix "cdt_" followed by alphanumeric characters.
   */
  uid: string;
  /**
   * A unique, identifying string that appears on the credit note and in places it is referenced.
   */
  creditNoteNumber: string;
  /**
   * Unique identifier for the credit note. It is generated automatically by Chargify and has the
   * prefix "cn_" followed by alphanumeric characters.
   */
  creditNoteUid: string;
  /** The full, original amount of the credit note. */
  originalAmount: string;
  /** The amount of the credit note applied to invoice. */
  appliedAmount: string;
  /** The time the credit note was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" */
  transactionTime?: Date;
  /** The credit note memo. */
  memo?: string | null;
  /** The role of the credit note (e.g. 'general') */
  role?: string;
  /** Shows whether it was applied to consolidated invoice or not. */
  consolidatedInvoice?: boolean;
  /** List of credit notes applied to children invoices (if consolidated invoice) */
  appliedCreditNotes?: AppliedCreditNoteData[];
};

export const applyCreditNoteEventDataSchema: Schema<ApplyCreditNoteEventData> =
  s.object<ApplyCreditNoteEventData>({
    uid: s.string(),
    creditNoteNumber: s.string(),
    creditNoteUid: s.string(),
    originalAmount: s.string(),
    appliedAmount: s.string(),
    transactionTime: s.optional(s.dateTime()),
    memo: s.optionalNullable(s.string()),
    role: s.optional(s.string()),
    consolidatedInvoice: s.optional(s.boolean()),
    appliedCreditNotes: s.optional(s.array(s.lazy(() => appliedCreditNoteDataSchema))),
    _keysMap: {
      creditNoteNumber: "credit_note_number",
      creditNoteUid: "credit_note_uid",
      originalAmount: "original_amount",
      appliedAmount: "applied_amount",
      transactionTime: "transaction_time",
      consolidatedInvoice: "consolidated_invoice",
      appliedCreditNotes: "applied_credit_notes",
    },
  });
