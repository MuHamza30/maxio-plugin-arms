import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ComponentCurrencyPrice = {
  id?: number;
  currency?: string;
  price?: string;
  formattedPrice?: string;
  priceId?: number;
  pricePointId?: number;
};

export const componentCurrencyPriceSchema: Schema<ComponentCurrencyPrice> = s.object<ComponentCurrencyPrice>({
  id: s.optional(s.int()),
  currency: s.optional(s.string()),
  price: s.optional(s.string()),
  formattedPrice: s.optional(s.string()),
  priceId: s.optional(s.int()),
  pricePointId: s.optional(s.int()),
  _keysMap: {
    formattedPrice: "formatted_price",
    priceId: "price_id",
    pricePointId: "price_point_id",
  },
});
