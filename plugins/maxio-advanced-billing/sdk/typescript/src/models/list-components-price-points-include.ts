import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ListComponentsPricePointsInclude = {
  CurrencyPrices: "currency_prices",
} as const;
export type ListComponentsPricePointsInclude =
  | (typeof ListComponentsPricePointsInclude)[keyof typeof ListComponentsPricePointsInclude]
  | (string & {});

export const listComponentsPricePointsIncludeSchema: EnumSchema<ListComponentsPricePointsInclude> =
  s.enumOf<ListComponentsPricePointsInclude>(ListComponentsPricePointsInclude);
