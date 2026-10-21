import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type Amount2 = string | number;

export const amount2Schema: Schema<Amount2> = s.of<Amount2>(s.union([s.string(), s.float64()]));
