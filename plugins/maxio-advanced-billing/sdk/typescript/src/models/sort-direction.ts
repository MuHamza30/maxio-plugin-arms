import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SortDirection = {
  Asc: "asc",
  Desc: "desc",
} as const;
export type SortDirection = (typeof SortDirection)[keyof typeof SortDirection] | (string & {});

export const sortDirectionSchema: EnumSchema<SortDirection> = s.enumOf<SortDirection>(SortDirection);
