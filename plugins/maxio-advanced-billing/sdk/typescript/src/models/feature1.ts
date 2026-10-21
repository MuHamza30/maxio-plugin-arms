import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  entitlementPeriodicityUnitSchema,
  type EntitlementPeriodicityUnit,
} from "./entitlement-periodicity-unit.js";
import { featureValueTypeSchema, type FeatureValueType } from "./feature-value-type.js";

/**
 * `key` cannot be changed once set. `kind` cannot be changed once any feature catalog item has been
 * created from this template.
 */
export type Feature1 = {
  name?: string;
  description?: string | null;
  unit?: string | null;
  /**
   * The data type of a feature's value. For `access_right` features this is always `boolean`, and
   * for `usage_limit` features this is always `numeric`. For `service_right` features, you choose
   * the value type explicitly.
   */
  valueType?: FeatureValueType;
  defaultValue?: string | null;
  defaultPeriodicityInterval?: number | null;
  defaultPeriodicityUnit?: EntitlementPeriodicityUnit | null;
};

export const feature1Schema: Schema<Feature1> = s.object<Feature1>({
  name: s.optional(s.string()),
  description: s.optionalNullable(s.string()),
  unit: s.optionalNullable(s.string()),
  valueType: s.optional(s.lazy(() => featureValueTypeSchema)),
  defaultValue: s.optionalNullable(s.string()),
  defaultPeriodicityInterval: s.optionalNullable(s.int()),
  defaultPeriodicityUnit: s.optionalNullable(s.lazy(() => entitlementPeriodicityUnitSchema)),
  _keysMap: {
    valueType: "value_type",
    defaultValue: "default_value",
    defaultPeriodicityInterval: "default_periodicity_interval",
    defaultPeriodicityUnit: "default_periodicity_unit",
  },
});
