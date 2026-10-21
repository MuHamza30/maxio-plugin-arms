import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** Allows to filter by `created_at` or `updated_at`. */
export const BasicDateField = {
  UpdatedAt: "updated_at",
  CreatedAt: "created_at",
} as const;
export type BasicDateField = (typeof BasicDateField)[keyof typeof BasicDateField] | (string & {});

export const basicDateFieldSchema: EnumSchema<BasicDateField> = s.enumOf<BasicDateField>(BasicDateField);
