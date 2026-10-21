import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const GroupStatus = {
  Ungrouped: "ungrouped",
  Grouped: "grouped",
} as const;
export type GroupStatus = (typeof GroupStatus)[keyof typeof GroupStatus] | (string & {});

export const groupStatusSchema: EnumSchema<GroupStatus> = s.enumOf<GroupStatus>(GroupStatus);
