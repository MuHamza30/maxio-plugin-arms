import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Example schema for an `apply_debit_note` event */
export type ApplyDebitNoteEventData = {
  /** A unique, identifying string that appears on the debit note and in places it is referenced. */
  debitNoteNumber: string;
  /**
   * Unique identifier for the debit note. It is generated automatically by Chargify and has the
   * prefix "db_" followed by alphanumeric characters.
   */
  debitNoteUid: string;
  /** The full, original amount of the debit note. */
  originalAmount: string;
  /** The amount of the debit note applied to invoice. */
  appliedAmount: string;
  /** The debit note memo. */
  memo?: string | null;
  /** The time the debit note was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" */
  transactionTime?: Date | null;
};

export const applyDebitNoteEventDataSchema: Schema<ApplyDebitNoteEventData> =
  s.object<ApplyDebitNoteEventData>({
    debitNoteNumber: s.string(),
    debitNoteUid: s.string(),
    originalAmount: s.string(),
    appliedAmount: s.string(),
    memo: s.optionalNullable(s.string()),
    transactionTime: s.optionalNullable(s.dateTime()),
    _keysMap: {
      debitNoteNumber: "debit_note_number",
      debitNoteUid: "debit_note_uid",
      originalAmount: "original_amount",
      appliedAmount: "applied_amount",
      transactionTime: "transaction_time",
    },
  });
