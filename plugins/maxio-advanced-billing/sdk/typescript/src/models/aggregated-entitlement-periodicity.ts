import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  entitlementPeriodicityUnitSchema,
  type EntitlementPeriodicityUnit,
} from "./entitlement-periodicity-unit.js";

export type AggregatedEntitlementPeriodicity = {
  interval?: number;
  /** The recurring window over which a `usage_limit` feature's allowance resets. */
  unit?: EntitlementPeriodicityUnit;
};

export const aggregatedEntitlementPeriodicitySchema: Schema<AggregatedEntitlementPeriodicity> =
  s.object<AggregatedEntitlementPeriodicity>({
    interval: s.optional(s.int()),
    unit: s.optional(s.lazy(() => entitlementPeriodicityUnitSchema)),
  });
