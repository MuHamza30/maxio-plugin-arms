import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * The allocated quantity that was in effect before this allocation was created. String for
 * components supporting fractional quantities
 */
export type PreviousQuantity = number | string;

export const previousQuantitySchema: Schema<PreviousQuantity> = s.of<PreviousQuantity>(
  s.union([s.int(), s.string()]),
);
