import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** Allows to filter by `not_null` or `null`. */
export const IncludeNullOrNotNull = {
  NotNull: "not_null",
  Null: "null",
} as const;
export type IncludeNullOrNotNull =
  | (typeof IncludeNullOrNotNull)[keyof typeof IncludeNullOrNotNull]
  | (string & {});

export const includeNullOrNotNullSchema: EnumSchema<IncludeNullOrNotNull> =
  s.enumOf<IncludeNullOrNotNull>(IncludeNullOrNotNull);
