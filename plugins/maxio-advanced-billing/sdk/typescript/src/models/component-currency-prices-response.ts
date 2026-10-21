import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentCurrencyPriceSchema, type ComponentCurrencyPrice } from "./component-currency-price.js";

export type ComponentCurrencyPricesResponse = {
  currencyPrices: ComponentCurrencyPrice[];
};

export const componentCurrencyPricesResponseSchema: Schema<ComponentCurrencyPricesResponse> =
  s.object<ComponentCurrencyPricesResponse>({
    currencyPrices: s.array(s.lazy(() => componentCurrencyPriceSchema)),
    _keysMap: {
      currencyPrices: "currency_prices",
    },
  });
