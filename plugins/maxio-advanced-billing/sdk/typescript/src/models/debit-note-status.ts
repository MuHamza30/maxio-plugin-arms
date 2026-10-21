import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** Current status of the debit note. */
export const DebitNoteStatus = {
  Open: "open",
  Applied: "applied",
  Banished: "banished",
  Paid: "paid",
} as const;
export type DebitNoteStatus = (typeof DebitNoteStatus)[keyof typeof DebitNoteStatus] | (string & {});

export const debitNoteStatusSchema: EnumSchema<DebitNoteStatus> = s.enumOf<DebitNoteStatus>(DebitNoteStatus);
