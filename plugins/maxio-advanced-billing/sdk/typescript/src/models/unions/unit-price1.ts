import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * The amount the customer will be charged per unit when the pricing scheme is “per_unit”. For
 * On/Off Components, this is the amount that the customer will be charged when they turn the
 * component on for the subscription. The price can contain up to 8 decimal places. e.g., 1.00 or
 * 0.0012 or 0.00000065
 */
export type UnitPrice1 = string | number;

export const unitPrice1Schema: Schema<UnitPrice1> = s.of<UnitPrice1>(s.union([s.string(), s.float64()]));
