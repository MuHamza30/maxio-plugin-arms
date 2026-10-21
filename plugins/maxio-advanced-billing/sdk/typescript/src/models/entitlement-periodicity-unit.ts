import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** The recurring window over which a `usage_limit` feature's allowance resets. */
export const EntitlementPeriodicityUnit = {
  Hour: "hour",
  Day: "day",
  Week: "week",
  Month: "month",
  Year: "year",
} as const;
export type EntitlementPeriodicityUnit =
  | (typeof EntitlementPeriodicityUnit)[keyof typeof EntitlementPeriodicityUnit]
  | (string & {});

export const entitlementPeriodicityUnitSchema: EnumSchema<EntitlementPeriodicityUnit> =
  s.enumOf<EntitlementPeriodicityUnit>(EntitlementPeriodicityUnit);
