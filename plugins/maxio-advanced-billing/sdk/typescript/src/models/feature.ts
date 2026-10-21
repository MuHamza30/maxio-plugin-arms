import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  entitlementPeriodicityUnitSchema,
  type EntitlementPeriodicityUnit,
} from "./entitlement-periodicity-unit.js";
import { featureKindSchema, type FeatureKind } from "./feature-kind.js";
import { featureValueTypeSchema, type FeatureValueType } from "./feature-value-type.js";

export type Feature = {
  /** A unique, lowercase, underscore-separated identifier for the feature. Immutable once set. */
  key: string;
  /** The display name of the feature. */
  name: string;
  description?: string | null;
  /**
   * The behavior of a feature:
   * - `access_right`: a boolean entitlement. A subscriber either has access or does not.
   * - `usage_limit`: a quantified allowance measured over a recurring period (for example, "10,000
   *   API calls per month").
   * - `service_right`: a free-form value (text, boolean, or number) that isn't a simple access flag
   *   or a metered limit.
   */
  kind: FeatureKind;
  /** Required when `kind` is `usage_limit`. */
  unit?: string | null;
  /**
   * Required when `kind` is `service_right`. Ignored for other kinds, where it is inferred
   * automatically.
   */
  valueType?: FeatureValueType;
  defaultValue?: string | null;
  /** Only valid when `kind` is `usage_limit`. */
  defaultPeriodicityInterval?: number | null;
  /**
   * Only valid when `kind` is `usage_limit`. Must be set together with
   * `default_periodicity_interval`.
   */
  defaultPeriodicityUnit?: EntitlementPeriodicityUnit | null;
};

export const featureSchema: Schema<Feature> = s.object<Feature>({
  key: s.string(),
  name: s.string(),
  description: s.optionalNullable(s.string()),
  kind: featureKindSchema,
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
