import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreateCurrencyPrice = {
  /** ISO code for a currency defined on the site level */
  currency?: string;
  /** Price for the price level in this currency */
  price?: number;
  /** ID of the price that this corresponds with */
  priceId?: number;
};

export const createCurrencyPriceSchema: Schema<CreateCurrencyPrice> = s.object<CreateCurrencyPrice>({
  currency: s.optional(s.string()),
  price: s.optional(s.float64()),
  priceId: s.optional(s.int()),
  _keysMap: {
    priceId: "price_id",
  },
});
