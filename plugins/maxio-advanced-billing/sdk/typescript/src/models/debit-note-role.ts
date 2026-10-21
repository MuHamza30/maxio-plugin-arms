import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** The role of the debit note. */
export const DebitNoteRole = {
  Chargeback: "chargeback",
  Refund: "refund",
} as const;
export type DebitNoteRole = (typeof DebitNoteRole)[keyof typeof DebitNoteRole] | (string & {});

export const debitNoteRoleSchema: EnumSchema<DebitNoteRole> = s.enumOf<DebitNoteRole>(DebitNoteRole);
