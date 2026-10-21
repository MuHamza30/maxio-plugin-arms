import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createProductPricePointSchema, type CreateProductPricePoint } from "./create-product-price-point.js";

export type CreateProductPricePointRequest = {
  pricePoint: CreateProductPricePoint;
};

export const createProductPricePointRequestSchema: Schema<CreateProductPricePointRequest> =
  s.object<CreateProductPricePointRequest>({
    pricePoint: createProductPricePointSchema,
    _keysMap: {
      pricePoint: "price_point",
    },
  });
