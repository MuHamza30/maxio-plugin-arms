import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type ProductFamilyId = string | number;

export const productFamilyIdSchema: Schema<ProductFamilyId> = s.of<ProductFamilyId>(
  s.union([s.string(), s.int()]),
);
