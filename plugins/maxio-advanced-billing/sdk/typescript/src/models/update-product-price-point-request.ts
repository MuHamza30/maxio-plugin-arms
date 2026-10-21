import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateProductPricePointSchema, type UpdateProductPricePoint } from "./update-product-price-point.js";

export type UpdateProductPricePointRequest = {
  pricePoint: UpdateProductPricePoint;
};

export const updateProductPricePointRequestSchema: Schema<UpdateProductPricePointRequest> =
  s.object<UpdateProductPricePointRequest>({
    pricePoint: updateProductPricePointSchema,
    _keysMap: {
      pricePoint: "price_point",
    },
  });
