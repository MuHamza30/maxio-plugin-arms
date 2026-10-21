import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  entitlementPeriodicityUnitSchema,
  type EntitlementPeriodicityUnit,
} from "./entitlement-periodicity-unit.js";
import { featureKindSchema, type FeatureKind } from "./feature-kind.js";
import { featureValueTypeSchema, type FeatureValueType } from "./feature-value-type.js";

/**
 * A feature that can be granted to subscribers, defined once at the site level and then attached to
 * products or components.
 */
export type FeatureTemplate = {
  /** The Advanced Billing id of the feature template. */
  id?: number;
  /** A unique, lowercase, underscore-separated identifier for the feature. Immutable once set. */
  key?: string;
  /** The display name of the feature. */
  name?: string;
  description?: string | null;
  /**
   * The behavior of a feature:
   * - `access_right`: a boolean entitlement. A subscriber either has access or does not.
   * - `usage_limit`: a quantified allowance measured over a recurring period (for example, "10,000
   *   API calls per month").
   * - `service_right`: a free-form value (text, boolean, or number) that isn't a simple access flag
   *   or a metered limit.
   */
  kind?: FeatureKind;
  /**
   * The unit the feature is measured in (for example, `requests` or `GB`). Required when `kind` is
   * `usage_limit`.
   */
  unit?: string | null;
  /**
   * The data type of a feature's value. For `access_right` features this is always `boolean`, and
   * for `usage_limit` features this is always `numeric`. For `service_right` features, you choose
   * the value type explicitly.
   */
  valueType?: FeatureValueType;
  /** A default value used to pre-populate new feature catalog items created from this template. */
  defaultValue?: string | null;
  /**
   * For `usage_limit` features, the default periodicity interval used to pre-populate new feature
   * catalog items. Always `null` for other kinds.
   */
  defaultPeriodicityInterval?: number | null;
  /**
   * For `usage_limit` features, the default periodicity unit used to pre-populate new feature
   * catalog items. Always `null` for other kinds.
   */
  defaultPeriodicityUnit?: EntitlementPeriodicityUnit | null;
  /** The date and time the feature template was archived, or `null` if it is active. */
  archivedAt?: Date | null;
  createdAt?: Date;
  updatedAt?: Date;
  /**
   * The number of **components** this feature template is currently attached to via an active
   * feature catalog item. Despite the name, this counts components, not products. In the Advanced
   * Billing UI, components are labeled "Products."
   */
  productsCount?: number;
  /**
   * The number of **products** this feature template is currently attached to via an active feature
   * catalog item. Despite the name, this counts products, not plans. In the Advanced Billing UI,
   * products are labeled "Plans."
   */
  plansCount?: number;
};

export const featureTemplateSchema: Schema<FeatureTemplate> = s.object<FeatureTemplate>({
  id: s.optional(s.int()),
  key: s.optional(s.string()),
  name: s.optional(s.string()),
  description: s.optionalNullable(s.string()),
  kind: s.optional(s.lazy(() => featureKindSchema)),
  unit: s.optionalNullable(s.string()),
  valueType: s.optional(s.lazy(() => featureValueTypeSchema)),
  defaultValue: s.optionalNullable(s.string()),
  defaultPeriodicityInterval: s.optionalNullable(s.int()),
  defaultPeriodicityUnit: s.optionalNullable(s.lazy(() => entitlementPeriodicityUnitSchema)),
  archivedAt: s.optionalNullable(s.dateTime()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  productsCount: s.optional(s.int()),
  plansCount: s.optional(s.int()),
  _keysMap: {
    valueType: "value_type",
    defaultValue: "default_value",
    defaultPeriodicityInterval: "default_periodicity_interval",
    defaultPeriodicityUnit: "default_periodicity_unit",
    archivedAt: "archived_at",
    createdAt: "created_at",
    updatedAt: "updated_at",
    productsCount: "products_count",
    plansCount: "plans_count",
  },
});
