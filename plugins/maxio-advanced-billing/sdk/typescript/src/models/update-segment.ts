import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  createOrUpdateSegmentPriceSchema,
  type CreateOrUpdateSegmentPrice,
} from "./create-or-update-segment-price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

export type UpdateSegment = {
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme: PricingScheme;
  prices?: CreateOrUpdateSegmentPrice[];
};

export const updateSegmentSchema: Schema<UpdateSegment> = s.object<UpdateSegment>({
  pricingScheme: pricingSchemeSchema,
  prices: s.optional(s.array(s.lazy(() => createOrUpdateSegmentPriceSchema))),
  _keysMap: {
    pricingScheme: "pricing_scheme",
  },
});
