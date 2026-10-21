import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentPricePointSchema, type ComponentPricePoint } from "./component-price-point.js";

export type ListComponentsPricePointsResponse = {
  pricePoints: ComponentPricePoint[];
};

export const listComponentsPricePointsResponseSchema: Schema<ListComponentsPricePointsResponse> =
  s.object<ListComponentsPricePointsResponse>({
    pricePoints: s.array(s.lazy(() => componentPricePointSchema)),
    _keysMap: {
      pricePoints: "price_points",
    },
  });
