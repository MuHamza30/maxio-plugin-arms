import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ProductPricePointErrors = {
  pricePoint?: string;
  interval?: string[];
  intervalUnit?: string[];
  name?: string[];
  price?: string[];
  priceInCents?: string[];
};

export const productPricePointErrorsSchema: Schema<ProductPricePointErrors> =
  s.object<ProductPricePointErrors>({
    pricePoint: s.optional(s.string()),
    interval: s.optional(s.array(s.string())),
    intervalUnit: s.optional(s.array(s.string())),
    name: s.optional(s.array(s.string())),
    price: s.optional(s.array(s.string())),
    priceInCents: s.optional(s.array(s.string())),
    _keysMap: {
      pricePoint: "price_point",
      intervalUnit: "interval_unit",
      priceInCents: "price_in_cents",
    },
  });
