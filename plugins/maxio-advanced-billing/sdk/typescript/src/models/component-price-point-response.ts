import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentPricePointSchema, type ComponentPricePoint } from "./component-price-point.js";

export type ComponentPricePointResponse = {
  pricePoint: ComponentPricePoint;
};

export const componentPricePointResponseSchema: Schema<ComponentPricePointResponse> =
  s.object<ComponentPricePointResponse>({
    pricePoint: componentPricePointSchema,
    _keysMap: {
      pricePoint: "price_point",
    },
  });
