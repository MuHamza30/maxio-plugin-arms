import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ListProductsInclude = {
  PrepaidProductPricePoint: "prepaid_product_price_point",
} as const;
export type ListProductsInclude =
  | (typeof ListProductsInclude)[keyof typeof ListProductsInclude]
  | (string & {});

export const listProductsIncludeSchema: EnumSchema<ListProductsInclude> =
  s.enumOf<ListProductsInclude>(ListProductsInclude);
