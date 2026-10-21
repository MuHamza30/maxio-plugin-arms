import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  cloneComponentPricePointSchema,
  type CloneComponentPricePoint,
} from "./clone-component-price-point.js";

export type CloneComponentPricePointRequest = {
  pricePoint: CloneComponentPricePoint;
};

export const cloneComponentPricePointRequestSchema: Schema<CloneComponentPricePointRequest> =
  s.object<CloneComponentPricePointRequest>({
    pricePoint: cloneComponentPricePointSchema,
    _keysMap: {
      pricePoint: "price_point",
    },
  });
