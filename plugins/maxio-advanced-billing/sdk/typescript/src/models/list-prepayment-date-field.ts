import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ListPrepaymentDateField = {
  CreatedAt: "created_at",
  ApplicationAt: "application_at",
} as const;
export type ListPrepaymentDateField =
  | (typeof ListPrepaymentDateField)[keyof typeof ListPrepaymentDateField]
  | (string & {});

export const listPrepaymentDateFieldSchema: EnumSchema<ListPrepaymentDateField> =
  s.enumOf<ListPrepaymentDateField>(ListPrepaymentDateField);
