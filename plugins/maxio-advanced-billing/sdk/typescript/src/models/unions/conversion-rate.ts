import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * How many wallet units one meter unit is worth, as a decimal string with at most 8 fractional
 * digits, greater than `0` and below 10^16. Send fractional values as strings: a JSON number with a
 * decimal point is rejected with `422`, because a double-precision float may already have lost
 * precision before the request arrives. Only meaningful with `meter_id`. Defaults to `"1.0"`.
 * Immutable once the wallet is created.
 */
export type ConversionRate = string | number;

export const conversionRateSchema: Schema<ConversionRate> = s.of<ConversionRate>(
  s.union([s.string(), s.int()]),
);
