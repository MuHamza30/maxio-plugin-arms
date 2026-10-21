import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type ProductIdModel = number | string;

export const productIdModelSchema: Schema<ProductIdModel> = s.of<ProductIdModel>(
  s.union([s.int(), s.string()]),
);
