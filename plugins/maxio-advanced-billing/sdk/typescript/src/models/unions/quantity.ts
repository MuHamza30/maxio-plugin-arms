import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * The allocated quantity set into effect by the allocation. String for components supporting
 * fractional quantities
 */
export type Quantity = number | string;

export const quantitySchema: Schema<Quantity> = s.of<Quantity>(s.union([s.int(), s.string()]));
