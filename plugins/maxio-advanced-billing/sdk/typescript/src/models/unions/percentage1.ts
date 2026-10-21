import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type Percentage1 = string | number;

export const percentage1Schema: Schema<Percentage1> = s.of<Percentage1>(s.union([s.string(), s.float64()]));
