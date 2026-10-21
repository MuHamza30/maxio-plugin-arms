import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** Current status of the credit note. */
export const CreditNoteStatus = {
  Open: "open",
  Applied: "applied",
} as const;
export type CreditNoteStatus = (typeof CreditNoteStatus)[keyof typeof CreditNoteStatus] | (string & {});

export const creditNoteStatusSchema: EnumSchema<CreditNoteStatus> =
  s.enumOf<CreditNoteStatus>(CreditNoteStatus);
