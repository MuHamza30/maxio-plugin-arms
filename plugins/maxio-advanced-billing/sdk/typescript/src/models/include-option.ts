import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const IncludeOption = {
  _0: "0",
  _1: "1",
} as const;
export type IncludeOption = (typeof IncludeOption)[keyof typeof IncludeOption] | (string & {});

export const includeOptionSchema: EnumSchema<IncludeOption> = s.enumOf<IncludeOption>(IncludeOption);
