import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type PricePointIdModel = number | string;

export const pricePointIdModelSchema: Schema<PricePointIdModel> = s.of<PricePointIdModel>(
  s.union([s.int(), s.string()]),
);
