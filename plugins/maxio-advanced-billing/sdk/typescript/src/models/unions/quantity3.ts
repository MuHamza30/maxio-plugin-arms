import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * The quantity can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065. If you
 * submit a value with more than 8 decimal places, we will round it down to the 8th decimal place.
 */
export type Quantity3 = number | string;

export const quantity3Schema: Schema<Quantity3> = s.of<Quantity3>(s.union([s.float64(), s.string()]));
