import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const FirstChargeType = {
  Prorated: "prorated",
  Immediate: "immediate",
  Delayed: "delayed",
} as const;
export type FirstChargeType = (typeof FirstChargeType)[keyof typeof FirstChargeType] | (string & {});

export const firstChargeTypeSchema: EnumSchema<FirstChargeType> = s.enumOf<FirstChargeType>(FirstChargeType);
