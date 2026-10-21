import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * Required when creating a new percentage coupon. Can't be used together with amount_in_cents.
 * Percentage discount.
 */
export type Percentage = string | number;

export const percentageSchema: Schema<Percentage> = s.of<Percentage>(s.union([s.string(), s.float64()]));
