import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type UpdateProductPricePoint = {
  handle?: string;
  priceInCents?: number;
};

export const updateProductPricePointSchema: Schema<UpdateProductPricePoint> =
  s.object<UpdateProductPricePoint>({
    handle: s.optional(s.string()),
    priceInCents: s.optional(s.int()),
    _keysMap: {
      priceInCents: "price_in_cents",
    },
  });
