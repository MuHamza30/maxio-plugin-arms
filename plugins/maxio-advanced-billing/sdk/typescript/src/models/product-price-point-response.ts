import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { productPricePointSchema, type ProductPricePoint } from "./product-price-point.js";

export type ProductPricePointResponse = {
  pricePoint: ProductPricePoint;
};

export const productPricePointResponseSchema: Schema<ProductPricePointResponse> =
  s.object<ProductPricePointResponse>({
    pricePoint: productPricePointSchema,
    _keysMap: {
      pricePoint: "price_point",
    },
  });
