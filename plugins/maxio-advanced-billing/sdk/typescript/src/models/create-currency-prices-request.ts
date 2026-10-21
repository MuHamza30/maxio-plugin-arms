import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createCurrencyPriceSchema, type CreateCurrencyPrice } from "./create-currency-price.js";

export type CreateCurrencyPricesRequest = {
  currencyPrices: CreateCurrencyPrice[];
};

export const createCurrencyPricesRequestSchema: Schema<CreateCurrencyPricesRequest> =
  s.object<CreateCurrencyPricesRequest>({
    currencyPrices: s.array(s.lazy(() => createCurrencyPriceSchema)),
    _keysMap: {
      currencyPrices: "currency_prices",
    },
  });
