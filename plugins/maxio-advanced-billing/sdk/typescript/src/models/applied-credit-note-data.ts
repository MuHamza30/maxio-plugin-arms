import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type AppliedCreditNoteData = {
  /** The UID of the credit note */
  uid?: string;
  /** The number of the credit note */
  number?: string;
};

export const appliedCreditNoteDataSchema: Schema<AppliedCreditNoteData> = s.object<AppliedCreditNoteData>({
  uid: s.optional(s.string()),
  number: s.optional(s.string()),
});
