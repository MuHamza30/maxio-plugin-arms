import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { productPricePointSchema, type ProductPricePoint } from "./product-price-point.js";

export type BulkCreateProductPricePointsResponse = {
  pricePoints?: ProductPricePoint[];
};

export const bulkCreateProductPricePointsResponseSchema: Schema<BulkCreateProductPricePointsResponse> =
  s.object<BulkCreateProductPricePointsResponse>({
    pricePoints: s.optional(s.array(s.lazy(() => productPricePointSchema))),
    _keysMap: {
      pricePoints: "price_points",
    },
  });
