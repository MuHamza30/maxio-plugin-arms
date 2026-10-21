import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** A string of the dollar amount to be refunded (eg. "10.50" => $10.50) */
export type Amount = string | number;

export const amountSchema: Schema<Amount> = s.of<Amount>(s.union([s.string(), s.float64()]));
