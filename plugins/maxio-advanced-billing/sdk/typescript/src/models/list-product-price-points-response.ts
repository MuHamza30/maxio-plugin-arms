import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { productPricePointSchema, type ProductPricePoint } from "./product-price-point.js";

export type ListProductPricePointsResponse = {
  pricePoints: ProductPricePoint[];
};

export const listProductPricePointsResponseSchema: Schema<ListProductPricePointsResponse> =
  s.object<ListProductPricePointsResponse>({
    pricePoints: s.array(s.lazy(() => productPricePointSchema)),
    _keysMap: {
      pricePoints: "price_points",
    },
  });
