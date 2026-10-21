import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { pricePointSchema, type PricePoint } from "./unions/price-point.js";

export type CreateComponentPricePointsRequest = {
  pricePoints: PricePoint[];
};

export const createComponentPricePointsRequestSchema: Schema<CreateComponentPricePointsRequest> =
  s.object<CreateComponentPricePointsRequest>({
    pricePoints: s.array(s.lazy(() => pricePointSchema)),
    _keysMap: {
      pricePoints: "price_points",
    },
  });
