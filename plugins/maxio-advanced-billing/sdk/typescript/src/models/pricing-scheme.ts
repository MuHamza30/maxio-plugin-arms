import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The identifier for the pricing scheme. See [Product
 * Components](https://help.chargify.com/products/product-components.html) for an overview of
 * pricing schemes.
 */
export const PricingScheme = {
  Stairstep: "stairstep",
  Volume: "volume",
  PerUnit: "per_unit",
  Tiered: "tiered",
} as const;
export type PricingScheme = (typeof PricingScheme)[keyof typeof PricingScheme] | (string & {});

export const pricingSchemeSchema: EnumSchema<PricingScheme> = s.enumOf<PricingScheme>(PricingScheme);
