import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * Identifies which kind of price point a feature catalog item override applies to:
 * `ProductPricePoint` for a product price point, `PricePoint` for a component price point. Only
 * relevant when `price_point_id` is set.
 */
export const FeatureOwnerPricePointType = {
  ProductPricePoint: "ProductPricePoint",
  PricePoint: "PricePoint",
} as const;
export type FeatureOwnerPricePointType =
  | (typeof FeatureOwnerPricePointType)[keyof typeof FeatureOwnerPricePointType]
  | (string & {});

export const featureOwnerPricePointTypeSchema: EnumSchema<FeatureOwnerPricePointType> =
  s.enumOf<FeatureOwnerPricePointType>(FeatureOwnerPricePointType);
