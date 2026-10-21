import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * The amount the customer will be charged per unit when the pricing scheme is “per_unit”. The price
 * can contain up to 8 decimal places. i.e., 1.00 or 0.0012 or 0.00000065
 */
export type UnitPrice5 = string | number;

export const unitPrice5Schema: Schema<UnitPrice5> = s.of<UnitPrice5>(s.union([s.string(), s.float64()]));
