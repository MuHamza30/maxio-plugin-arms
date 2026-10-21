import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  entitlementPeriodicityUnitSchema,
  type EntitlementPeriodicityUnit,
} from "./entitlement-periodicity-unit.js";
import { featureKindSchema, type FeatureKind } from "./feature-kind.js";
import {
  featureOwnerPricePointTypeSchema,
  type FeatureOwnerPricePointType,
} from "./feature-owner-price-point-type.js";

/**
 * A feature template attached to a specific product or component (or one of their price points),
 * with a concrete value. When a subscriber signs up for or is assigned this product/component, the
 * feature catalog item is provisioned as an entitlement on their subscription.
 */
export type FeatureCatalogItem = {
  id?: number;
  /** The id of the feature template this item was created from. */
  featureTemplateId?: number;
  /** The `key` of the parent feature template. */
  featureKey?: string;
  /** The `name` of the parent feature template. */
  featureName?: string;
  /**
   * The behavior of a feature:
   * - `access_right`: a boolean entitlement. A subscriber either has access or does not.
   * - `usage_limit`: a quantified allowance measured over a recurring period (for example, "10,000
   *   API calls per month").
   * - `service_right`: a free-form value (text, boolean, or number) that isn't a simple access flag
   *   or a metered limit.
   */
  featureKind?: FeatureKind;
  /**
   * The value granted by this feature catalog item. Interpreted according to `feature_kind`:
   * `"true"`/`"false"` for `access_right`, a numeric string for `usage_limit`, or any string for
   * `service_right` (shaped by the feature template's `value_type`).
   */
  value?: string;
  /** Set when `feature_kind` is `usage_limit`; `null` otherwise. */
  periodicityInterval?: number | null;
  /** Set when `feature_kind` is `usage_limit`; `null` otherwise. */
  periodicityUnit?: EntitlementPeriodicityUnit | null;
  /**
   * `null` when this feature catalog item applies to every price point of its owning
   * product/component. Set when the feature catalog item is an override for one specific price
   * point.
   */
  pricePointType?: FeatureOwnerPricePointType | null;
  /** Set together with `price_point_type` for price-point-specific overrides. */
  pricePointId?: number | null;
  archivedAt?: Date | null;
  createdAt?: Date;
  updatedAt?: Date;
};

export const featureCatalogItemSchema: Schema<FeatureCatalogItem> = s.object<FeatureCatalogItem>({
  id: s.optional(s.int()),
  featureTemplateId: s.optional(s.int()),
  featureKey: s.optional(s.string()),
  featureName: s.optional(s.string()),
  featureKind: s.optional(s.lazy(() => featureKindSchema)),
  value: s.optional(s.string()),
  periodicityInterval: s.optionalNullable(s.int()),
  periodicityUnit: s.optionalNullable(s.lazy(() => entitlementPeriodicityUnitSchema)),
  pricePointType: s.optionalNullable(s.lazy(() => featureOwnerPricePointTypeSchema)),
  pricePointId: s.optionalNullable(s.int()),
  archivedAt: s.optionalNullable(s.dateTime()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  _keysMap: {
    featureTemplateId: "feature_template_id",
    featureKey: "feature_key",
    featureName: "feature_name",
    featureKind: "feature_kind",
    periodicityInterval: "periodicity_interval",
    periodicityUnit: "periodicity_unit",
    pricePointType: "price_point_type",
    pricePointId: "price_point_id",
    archivedAt: "archived_at",
    createdAt: "created_at",
    updatedAt: "updated_at",
  },
});
