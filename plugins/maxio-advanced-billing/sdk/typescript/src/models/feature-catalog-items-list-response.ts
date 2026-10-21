import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { featureCatalogItemSchema, type FeatureCatalogItem } from "./feature-catalog-item.js";

export type FeatureCatalogItemsListResponse = {
  features: FeatureCatalogItem[];
  /**
   * The number of subscriptions on this product/component that would be affected if a feature
   * catalog item change were propagated with `propagate_to_subscriptions=true`.
   */
  subscriptionsCount: number;
};

export const featureCatalogItemsListResponseSchema: Schema<FeatureCatalogItemsListResponse> =
  s.object<FeatureCatalogItemsListResponse>({
    features: s.array(s.lazy(() => featureCatalogItemSchema)),
    subscriptionsCount: s.int(),
    _keysMap: {
      subscriptionsCount: "subscriptions_count",
    },
  });
