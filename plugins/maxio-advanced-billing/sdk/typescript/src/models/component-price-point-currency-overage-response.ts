import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { currencyOveragePricesSchema, type CurrencyOveragePrices } from "./currency-overage-prices.js";

export type ComponentPricePointCurrencyOverageResponse = {
  /** Extends a component price point with currency overage prices. */
  pricePoint: CurrencyOveragePrices;
};

export const componentPricePointCurrencyOverageResponseSchema: Schema<ComponentPricePointCurrencyOverageResponse> =
  s.object<ComponentPricePointCurrencyOverageResponse>({
    pricePoint: currencyOveragePricesSchema,
    _keysMap: {
      pricePoint: "price_point",
    },
  });
