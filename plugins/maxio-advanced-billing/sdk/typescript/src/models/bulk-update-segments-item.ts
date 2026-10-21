import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  createOrUpdateSegmentPriceSchema,
  type CreateOrUpdateSegmentPrice,
} from "./create-or-update-segment-price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

export type BulkUpdateSegmentsItem = {
  /** The ID of the segment you want to update. */
  id: number;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme: PricingScheme;
  prices: CreateOrUpdateSegmentPrice[];
};

export const bulkUpdateSegmentsItemSchema: Schema<BulkUpdateSegmentsItem> = s.object<BulkUpdateSegmentsItem>({
  id: s.int(),
  pricingScheme: pricingSchemeSchema,
  prices: s.array(s.lazy(() => createOrUpdateSegmentPriceSchema)),
  _keysMap: {
    pricingScheme: "pricing_scheme",
  },
});
