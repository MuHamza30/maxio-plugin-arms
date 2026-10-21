import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  updateComponentPricePointSchema,
  type UpdateComponentPricePoint,
} from "./update-component-price-point.js";

export type UpdateComponentPricePointRequest = {
  pricePoint?: UpdateComponentPricePoint;
};

export const updateComponentPricePointRequestSchema: Schema<UpdateComponentPricePointRequest> =
  s.object<UpdateComponentPricePointRequest>({
    pricePoint: s.optional(s.lazy(() => updateComponentPricePointSchema)),
    _keysMap: {
      pricePoint: "price_point",
    },
  });
