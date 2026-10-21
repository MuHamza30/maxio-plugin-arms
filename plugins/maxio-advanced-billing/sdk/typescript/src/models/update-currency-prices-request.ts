import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateCurrencyPriceSchema, type UpdateCurrencyPrice } from "./update-currency-price.js";

export type UpdateCurrencyPricesRequest = {
  currencyPrices: UpdateCurrencyPrice[];
};

export const updateCurrencyPricesRequestSchema: Schema<UpdateCurrencyPricesRequest> =
  s.object<UpdateCurrencyPricesRequest>({
    currencyPrices: s.array(s.lazy(() => updateCurrencyPriceSchema)),
    _keysMap: {
      currencyPrices: "currency_prices",
    },
  });
