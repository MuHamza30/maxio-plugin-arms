import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentCustomPriceSchema, type ComponentCustomPrice } from "./component-custom-price.js";
import { priceSchema, type Price } from "./price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

/**
 * Used in place of `price_point_id` to define a custom price point unique to the subscription. You
 * still need to provide `component_id`.
 */
export type SubscriptionGroupComponentCustomPrice = {
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme?: PricingScheme;
  prices?: Price[];
  overagePricing?: ComponentCustomPrice[];
};

export const subscriptionGroupComponentCustomPriceSchema: Schema<SubscriptionGroupComponentCustomPrice> =
  s.object<SubscriptionGroupComponentCustomPrice>({
    pricingScheme: s.optional(s.lazy(() => pricingSchemeSchema)),
    prices: s.optional(s.array(s.lazy(() => priceSchema))),
    overagePricing: s.optional(s.array(s.lazy(() => componentCustomPriceSchema))),
    _keysMap: {
      pricingScheme: "pricing_scheme",
      overagePricing: "overage_pricing",
    },
  });
