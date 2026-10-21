import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { currencyPriceSchema, type CurrencyPrice } from "./currency-price.js";

export type CurrencyPricesResponse = {
  currencyPrices: CurrencyPrice[];
};

export const currencyPricesResponseSchema: Schema<CurrencyPricesResponse> = s.object<CurrencyPricesResponse>({
  currencyPrices: s.array(s.lazy(() => currencyPriceSchema)),
  _keysMap: {
    currencyPrices: "currency_prices",
  },
});
