import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ListEventsDateField = {
  CreatedAt: "created_at",
} as const;
export type ListEventsDateField =
  | (typeof ListEventsDateField)[keyof typeof ListEventsDateField]
  | (string & {});

export const listEventsDateFieldSchema: EnumSchema<ListEventsDateField> =
  s.enumOf<ListEventsDateField>(ListEventsDateField);
