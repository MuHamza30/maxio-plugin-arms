import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** `amount_in_cents` is not required if you pass `amount`. */
export type Amount5 = string | number;

export const amount5Schema: Schema<Amount5> = s.of<Amount5>(s.union([s.string(), s.float64()]));
