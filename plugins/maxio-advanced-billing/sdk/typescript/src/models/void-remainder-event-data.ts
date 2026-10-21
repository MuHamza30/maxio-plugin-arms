import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditNoteSchema, type CreditNote } from "./credit-note.js";

/** Example schema for an `void_remainder` event */
export type VoidRemainderEventData = {
  creditNoteAttributes: CreditNote;
  /** The memo provided during invoice remainder voiding. */
  memo: string;
  /** The amount of the void. */
  appliedAmount: string;
  /** The time the refund was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" */
  transactionTime: Date;
};

export const voidRemainderEventDataSchema: Schema<VoidRemainderEventData> = s.object<VoidRemainderEventData>({
  creditNoteAttributes: creditNoteSchema,
  memo: s.string(),
  appliedAmount: s.string(),
  transactionTime: s.dateTime(),
  _keysMap: {
    creditNoteAttributes: "credit_note_attributes",
    appliedAmount: "applied_amount",
    transactionTime: "transaction_time",
  },
});
