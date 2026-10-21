import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  entitlementPeriodicityUnitSchema,
  type EntitlementPeriodicityUnit,
} from "./entitlement-periodicity-unit.js";

export type Feature3 = {
  value?: string;
  periodicityInterval?: number | null;
  periodicityUnit?: EntitlementPeriodicityUnit | null;
  /**
   * When `true`, the new `value`/periodicity is immediately applied to every existing entitlement
   * created from this feature catalog item.
   *
   * @default false
   */
  propagateToSubscriptions?: boolean;
};

export const feature3Schema: Schema<Feature3> = s.object<Feature3>({
  value: s.optional(s.string()),
  periodicityInterval: s.optionalNullable(s.int()),
  periodicityUnit: s.optionalNullable(s.lazy(() => entitlementPeriodicityUnitSchema)),
  propagateToSubscriptions: s.defaulted(s.boolean(), false),
  _keysMap: {
    periodicityInterval: "periodicity_interval",
    periodicityUnit: "periodicity_unit",
    propagateToSubscriptions: "propagate_to_subscriptions",
  },
});
