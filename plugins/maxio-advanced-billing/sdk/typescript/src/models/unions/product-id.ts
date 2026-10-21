import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Product handle or product id. */
export type ProductId = string | number;

export const productIdSchema: Schema<ProductId> = s.of<ProductId>(s.union([s.string(), s.int()]));
