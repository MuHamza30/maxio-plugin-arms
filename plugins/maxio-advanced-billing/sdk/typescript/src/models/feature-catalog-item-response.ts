import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { featureCatalogItemSchema, type FeatureCatalogItem } from "./feature-catalog-item.js";

export type FeatureCatalogItemResponse = {
  /**
   * A feature template attached to a specific product or component (or one of their price points),
   * with a concrete value. When a subscriber signs up for or is assigned this product/component,
   * the feature catalog item is provisioned as an entitlement on their subscription.
   */
  feature: FeatureCatalogItem;
};

export const featureCatalogItemResponseSchema: Schema<FeatureCatalogItemResponse> =
  s.object<FeatureCatalogItemResponse>({
    feature: featureCatalogItemSchema,
  });
