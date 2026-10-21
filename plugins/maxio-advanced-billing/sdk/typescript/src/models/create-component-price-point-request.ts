import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { pricePointSchema, type PricePoint } from "./unions/price-point.js";

export type CreateComponentPricePointRequest = {
  pricePoint: PricePoint;
};

export const createComponentPricePointRequestSchema: Schema<CreateComponentPricePointRequest> =
  s.object<CreateComponentPricePointRequest>({
    pricePoint: pricePointSchema,
    _keysMap: {
      pricePoint: "price_point",
    },
  });
