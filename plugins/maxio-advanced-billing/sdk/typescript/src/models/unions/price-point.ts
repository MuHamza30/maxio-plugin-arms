import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import {
  createComponentPricePointSchema,
  type CreateComponentPricePoint,
} from "../create-component-price-point.js";
import {
  createPrepaidUsageComponentPricePointSchema,
  type CreatePrepaidUsageComponentPricePoint,
} from "../create-prepaid-usage-component-price-point.js";

export type PricePoint = CreateComponentPricePoint | CreatePrepaidUsageComponentPricePoint;

export const pricePointSchema: Schema<PricePoint> = s.of<PricePoint>(
  s.union([
    s.lazy(() => createComponentPricePointSchema),
    s.lazy(() => createPrepaidUsageComponentPricePointSchema),
  ]),
);
