import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type Amount3 = number | string;

export const amount3Schema: Schema<Amount3> = s.of<Amount3>(s.union([s.float64(), s.string()]));
