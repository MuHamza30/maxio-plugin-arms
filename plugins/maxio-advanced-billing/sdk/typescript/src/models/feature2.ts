import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  entitlementPeriodicityUnitSchema,
  type EntitlementPeriodicityUnit,
} from "./entitlement-periodicity-unit.js";
import {
  featureOwnerPricePointTypeSchema,
  type FeatureOwnerPricePointType,
} from "./feature-owner-price-point-type.js";

export type Feature2 = {
  /** The id of the feature template to attach. */
  featureTemplateId: number;
  value: string;
  periodicityInterval?: number | null;
  periodicityUnit?: EntitlementPeriodicityUnit | null;
  /**
   * Omit to have this feature catalog item apply to every price point of the product/component. Set
   * together with `price_point_id` to scope the feature catalog item to a single price point.
   */
  pricePointType?: FeatureOwnerPricePointType | null;
  pricePointId?: number | null;
  /**
   * When `true`, existing subscriptions on this product/component are immediately granted an
   * entitlement for this feature, instead of waiting for their next subscription change.
   *
   * @default false
   */
  propagateToSubscriptions?: boolean;
};

export const feature2Schema: Schema<Feature2> = s.object<Feature2>({
  featureTemplateId: s.int(),
  value: s.string(),
  periodicityInterval: s.optionalNullable(s.int()),
  periodicityUnit: s.optionalNullable(s.lazy(() => entitlementPeriodicityUnitSchema)),
  pricePointType: s.optionalNullable(s.lazy(() => featureOwnerPricePointTypeSchema)),
  pricePointId: s.optionalNullable(s.int()),
  propagateToSubscriptions: s.defaulted(s.boolean(), false),
  _keysMap: {
    featureTemplateId: "feature_template_id",
    periodicityInterval: "periodicity_interval",
    periodicityUnit: "periodicity_unit",
    pricePointType: "price_point_type",
    pricePointId: "price_point_id",
    propagateToSubscriptions: "propagate_to_subscriptions",
  },
});
