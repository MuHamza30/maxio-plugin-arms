import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * Price point type. We expose the following types:
 * 1. **default**: a price point that is marked as a default price for a certain product.
 * 2. **custom**: a custom price point.
 * 3. **catalog**: a price point that is **not** marked as a default price for a certain product and
 *    is **not** a custom one.
 */
export const PricePointType = {
  Catalog: "catalog",
  Default: "default",
  Custom: "custom",
} as const;
export type PricePointType = (typeof PricePointType)[keyof typeof PricePointType] | (string & {});

export const pricePointTypeSchema: EnumSchema<PricePointType> = s.enumOf<PricePointType>(PricePointType);
