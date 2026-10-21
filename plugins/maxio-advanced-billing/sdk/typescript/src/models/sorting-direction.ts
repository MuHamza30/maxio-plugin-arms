import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** Used for sorting results. */
export const SortingDirection = {
  Asc: "asc",
  Desc: "desc",
} as const;
export type SortingDirection = (typeof SortingDirection)[keyof typeof SortingDirection] | (string & {});

export const sortingDirectionSchema: EnumSchema<SortingDirection> =
  s.enumOf<SortingDirection>(SortingDirection);
