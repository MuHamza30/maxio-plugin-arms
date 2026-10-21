import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createProductPricePointSchema, type CreateProductPricePoint } from "./create-product-price-point.js";

export type BulkCreateProductPricePointsRequest = {
  pricePoints: CreateProductPricePoint[];
};

export const bulkCreateProductPricePointsRequestSchema: Schema<BulkCreateProductPricePointsRequest> =
  s.object<BulkCreateProductPricePointsRequest>({
    pricePoints: s.array(s.lazy(() => createProductPricePointSchema)),
    _keysMap: {
      pricePoints: "price_points",
    },
  });
