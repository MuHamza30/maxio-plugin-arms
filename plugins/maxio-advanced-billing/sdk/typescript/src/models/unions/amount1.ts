import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Dollar amount of the sum of the invoices payment (eg. "10.50" => $10.50). */
export type Amount1 = string | number;

export const amount1Schema: Schema<Amount1> = s.of<Amount1>(s.union([s.string(), s.float64()]));
