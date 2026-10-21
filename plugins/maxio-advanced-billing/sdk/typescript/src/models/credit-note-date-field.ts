import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const CreditNoteDateField = {
  IssueDate: "issue_date",
  AppliedDate: "applied_date",
  CreatedAt: "created_at",
  UpdatedAt: "updated_at",
} as const;
export type CreditNoteDateField =
  | (typeof CreditNoteDateField)[keyof typeof CreditNoteDateField]
  | (string & {});

export const creditNoteDateFieldSchema: EnumSchema<CreditNoteDateField> =
  s.enumOf<CreditNoteDateField>(CreditNoteDateField);
