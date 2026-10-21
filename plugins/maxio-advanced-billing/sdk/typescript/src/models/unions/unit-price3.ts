import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * This is the amount that the customer will be charged when they turn the component on for the
 * subscription. The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065
 */
export type UnitPrice3 = string | number;

export const unitPrice3Schema: Schema<UnitPrice3> = s.of<UnitPrice3>(s.union([s.string(), s.float64()]));
