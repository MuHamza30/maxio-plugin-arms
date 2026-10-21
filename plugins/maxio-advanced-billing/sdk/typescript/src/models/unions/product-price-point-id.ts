import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type ProductPricePointId = string | number;

export const productPricePointIdSchema: Schema<ProductPricePointId> = s.of<ProductPricePointId>(
  s.union([s.string(), s.int()]),
);
