import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  createProductCurrencyPriceSchema,
  type CreateProductCurrencyPrice,
} from "./create-product-currency-price.js";

export type CreateProductCurrencyPricesRequest = {
  currencyPrices: CreateProductCurrencyPrice[];
};

export const createProductCurrencyPricesRequestSchema: Schema<CreateProductCurrencyPricesRequest> =
  s.object<CreateProductCurrencyPricesRequest>({
    currencyPrices: s.array(s.lazy(() => createProductCurrencyPriceSchema)),
    _keysMap: {
      currencyPrices: "currency_prices",
    },
  });
