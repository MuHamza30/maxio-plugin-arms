import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * For Quantity-based components: The current allocation for the component on the given
 * subscription. For On/Off components: Use 1 for on. Use 0 for off.
 */
export type AllocatedQuantity2 = number | string;

export const allocatedQuantity2Schema: Schema<AllocatedQuantity2> = s.of<AllocatedQuantity2>(
  s.union([s.int(), s.string()]),
);
