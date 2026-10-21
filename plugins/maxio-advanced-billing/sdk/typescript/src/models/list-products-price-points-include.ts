import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ListProductsPricePointsInclude = {
  CurrencyPrices: "currency_prices",
} as const;
export type ListProductsPricePointsInclude =
  | (typeof ListProductsPricePointsInclude)[keyof typeof ListProductsPricePointsInclude]
  | (string & {});

export const listProductsPricePointsIncludeSchema: EnumSchema<ListProductsPricePointsInclude> =
  s.enumOf<ListProductsPricePointsInclude>(ListProductsPricePointsInclude);
