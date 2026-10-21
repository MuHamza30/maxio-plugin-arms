import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  componentCostDataRateTierSchema,
  type ComponentCostDataRateTier,
} from "./component-cost-data-rate-tier.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

export type ComponentCostData = {
  componentCodeId?: number | null;
  pricePointId?: number;
  productId?: number;
  quantity?: string;
  amount?: string;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme?: PricingScheme;
  tiers?: ComponentCostDataRateTier[];
};

export const componentCostDataSchema: Schema<ComponentCostData> = s.object<ComponentCostData>({
  componentCodeId: s.optionalNullable(s.int()),
  pricePointId: s.optional(s.int()),
  productId: s.optional(s.int()),
  quantity: s.optional(s.string()),
  amount: s.optional(s.string()),
  pricingScheme: s.optional(s.lazy(() => pricingSchemeSchema)),
  tiers: s.optional(s.array(s.lazy(() => componentCostDataRateTierSchema))),
  _keysMap: {
    componentCodeId: "component_code_id",
    pricePointId: "price_point_id",
    productId: "product_id",
    pricingScheme: "pricing_scheme",
  },
});
