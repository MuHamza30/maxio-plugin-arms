import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { currencyPriceRoleSchema, type CurrencyPriceRole } from "./currency-price-role.js";

export type CurrencyPrice = {
  id?: number;
  currency?: string;
  price?: number;
  formattedPrice?: string;
  priceId?: number;
  pricePointId?: number;
  productPricePointId?: number;
  /** Role for the price. */
  role?: CurrencyPriceRole;
};

export const currencyPriceSchema: Schema<CurrencyPrice> = s.object<CurrencyPrice>({
  id: s.optional(s.int()),
  currency: s.optional(s.string()),
  price: s.optional(s.float64()),
  formattedPrice: s.optional(s.string()),
  priceId: s.optional(s.int()),
  pricePointId: s.optional(s.int()),
  productPricePointId: s.optional(s.int()),
  role: s.optional(s.lazy(() => currencyPriceRoleSchema)),
  _keysMap: {
    formattedPrice: "formatted_price",
    priceId: "price_id",
    pricePointId: "price_point_id",
    productPricePointId: "product_price_point_id",
  },
});
